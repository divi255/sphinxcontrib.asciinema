__author__ = "Sergei S."
__copyright__ = "Copyright (C) 2019"
__license__ = "MIT"
__version__ = "0.1.1"

def setup(app):

    from . import asciinema

    app.add_node(asciinema.asciinema,
                 html=(asciinema.visit, asciinema.depart))
    app.add_directive('asciinema', asciinema.ASCIINemaDirective)
