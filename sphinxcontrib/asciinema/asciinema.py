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
    if node['type'] == 'local':
        template = '<asciinema-player {options} src="data:application/json;base64,{src}" />'
        option_template = '{}="{}" '
        src = node['content']
    else:
        template = ('<script id="asciicast-{src}" {options} '
                    'src="https://asciinema.org/a/{src}.js" async></script>')
        option_template = 'data-{}="{}" '
        src = node['content']
    options = ''
    for n, v in node['options'].items():
        options += option_template.format(n, v)
    tag = (template.format(options=options, src=src))
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
        'cols': directives.positive_int,
        'rows': directives.positive_int,
        'autoplay': directives.unchanged,
        'preload': directives.unchanged,
        'loop': directives.unchanged,
        'start-at': directives.unchanged,
        'speed': directives.unchanged,
        'idle-time-limit': directives.unchanged,
        'poster': directives.unchanged,
        'font-size': directives.unchanged,
        'size': directives.unchanged,
        'theme': directives.unchanged,
        'title': directives.unchanged,
        't': directives.unchanged,
        'author': directives.unchanged,
        'author-url': directives.unchanged,
        'author-img-url': directives.unchanged,
        'path': directives.unchanged,
    }
    required_arguments = 1
    optional_arguments = len(option_spec)

    def run(self):
        arg = self.arguments[0]
        options = dict(self.env.config['sphinxcontrib_asciinema_defaults'])
        options.update(self.options)
        kw = {'options': options}
        path = self.options.get('path', '')
        if path and not path.endswith('/'):
            path += '/'
        fname = arg if arg.startswith('./') else path + arg
        if self.is_file(fname):
            kw['content'] = self.to_b64(fname)
            kw['type'] = 'local'
            logger.debug('asciinema: added cast file %s' % fname)
        else:
            kw['content'] = arg
            kw['type'] = 'remote'
            logger.debug('asciinema: added cast id %s' % arg)
        if 'path ' in kw['options']:
            del kw['options']['path']
        return [Asciinema(**kw)]

    def is_file(self, rel_file):
        file_path = self.env.relfn2path(rel_file)[1]
        return os.path.isfile(file_path)

    def to_b64(self, filename):
        import base64
        with open(filename, 'rb') as file:
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
