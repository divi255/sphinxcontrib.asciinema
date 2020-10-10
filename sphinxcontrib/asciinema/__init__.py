__copyright__ = 'Copyright (C) 2019'
__license__ = 'MIT'
__version__ = "0.1.10"


def setup(app):
    from .asciinema import Asciinema, ASCIINemaDirective
    from .asciinema import copy_asset_files, visit_html, visit_man, depart

    app.add_config_value('sphinxcontrib_asciinema_defaults', {}, 'html')

    app.connect('build-finished', copy_asset_files)
    app.add_js_file('asciinema-player_2.6.1.js')
    app.add_css_file('asciinema-player_2.6.1.css')
    app.add_css_file('asciinema-custom.css')

    app.add_node(Asciinema, man=(visit_man, depart), html=(visit_html, depart))
    app.add_directive('asciinema', ASCIINemaDirective)
