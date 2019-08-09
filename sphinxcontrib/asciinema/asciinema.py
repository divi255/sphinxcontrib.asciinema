__author__ = "Sergei S. (https://makeitwork.cz/)"
__copyright__ = "Copyright (C) 2019"
__license__ = "MIT"
__version__ = "0.1.3"

from docutils import nodes
from docutils.parsers import rst


def setup(app):

    from . import asciinema

    app.add_node(asciinema.asciinema, html=(asciinema.visit, asciinema.depart))
    app.add_directive('asciinema', asciinema.ASCIINemaDirective)


class asciinema(nodes.General, nodes.Element):

    video_id = None


def visit(self, node):

    tag = ('<script id="asciicast-{}" ' +
           'src="https://asciinema.org/a/{}.js" async></script>').format(
               node.video_id, node.video_id)

    self.body.append(tag)


def depart(self, node):
    pass


class ASCIINemaDirective(rst.Directive):

    name = 'asciinema'
    node_class = asciinema

    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}

    def run(self):

        node = self.node_class()

        arg = self.arguments[0]

        if arg.startswith('http'):
            node.video_id = arg.split('/', 1)[-1]
        else:
            node.video_id = arg

        return [node]
