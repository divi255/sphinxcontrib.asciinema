import os

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.fileutil import copy_asset
from sphinx.util.docutils import SphinxDirective
from sphinx.util import logging

logger = logging.getLogger(__name__)


def copy_asset_files(app, exc):
    asset_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             '_static')
    if exc is None:  # build succeeded
        for file in os.listdir(asset_dir):
            copy_asset(os.path.join(asset_dir, file),
                       os.path.join(app.outdir, '_static'))


class Asciinema(nodes.General, nodes.Element):
    pass


def visit_html(self, node):
    rst_to_js_option_names: dict[str, str] = {
        "terminalfontsize": "terminalFontSize",
        "terminallineheigth": "terminalLineHeigth",
        "terminalfontfamily": "terminalFontFamily",
    }

    gen = (
        (rst_option_name, js_option_name)
        for (rst_option_name, js_option_name) in rst_to_js_option_names.items()
        if rst_option_name in node["options"]
    )
    for rst_option_name, js_option_name in gen:
        node["options"][js_option_name] = node["options"].pop(rst_option_name)

    load = """<script src="../_static/asciinema-player_3.6.3.js"></script>"""
    template = """<div id="asciicast-{src}" src></div>\n<script>\nAsciinemaPlayer.create("{src}", document.getElementById('asciicast-{src}'), {{{options} }});\n</script>\n"""
    option_template = '{}: "{}", '
    src = node["content"]
    options = ""
    for n, v in node["options"].items():
        options += option_template.format(n, v)
    tag = template.format(options=options, src=src)
    self.body.append(load)
    self.body.append(tag)


def visit_unsupported(self, node):
    logger.warning('asciinema: unsupported output format (node skipped)')
    raise nodes.SkipNode


def depart(self, node):
    pass


class ASCIINemaDirective(SphinxDirective):
    has_content = True
    final_argument_whitespace = False
    option_spec = {
        "cols": directives.positive_int,
        "rows": directives.positive_int,
        "autoplay": directives.unchanged,
        "preload": directives.unchanged,
        "loop": directives.unchanged,
        "start-at": directives.unchanged,
        "speed": directives.unchanged,
        "idle-time-limit": directives.unchanged,
        "theme": directives.unchanged,
        "poster": directives.unchanged,
        "fit": directives.unchanged,
        "controls": directives.unchanged,
        "markers": directives.unchanged,
        "pauseOnMarkers": directives.unchanged,
        "terminalfontsize": directives.unchanged,
        "terminalfontfamily": directives.unchanged,
        "terminallineheight": directives.unchanged,
        "path": directives.unchanged,
    }
    required_arguments = 1
    optional_arguments = len(option_spec)

    def run(self):
        arg = self.arguments[0]
        options = dict(self.env.config['sphinxcontrib_asciinema_defaults'])
        options.update(self.options)
        kw = {'options': options}
        path = options.get('path', '')
        if path and not path.endswith('/'):
            path += '/'
        fname = arg if arg.startswith('./') else path + arg
        if self.is_file(fname):
            kw['content'] = fname
            kw['type'] = 'local'
            logger.debug('asciinema: added cast file %s' % fname)
        else:
            kw['content'] = arg
            kw['type'] = 'remote'
            logger.debug('asciinema: added cast id %s' % arg)
        if 'path' in kw['options']:
            del kw['options']['path']
        return [Asciinema(**kw)]

    def is_file(self, rel_file):
        file_path = self.env.relfn2path(rel_file)[1]
        return os.path.isfile(file_path)

    def to_b64(self, filename):
        import base64
        file_path = self.env.relfn2path(filename)[1]
        with open(file_path, 'rb') as file:
            content = file.read()
        b64encoded = base64.b64encode(content)
        return b64encoded.decode()


_NODE_VISITORS = {
    'html': (visit_html, depart),
    'latex': (visit_unsupported, None),
    'man': (visit_unsupported, None),
    'texinfo': (visit_unsupported, None),
    'text': (visit_unsupported, None)
}
