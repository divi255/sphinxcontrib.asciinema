# sphinxcontrib-asciinema

Easily embed [asciinema](https://asciinema.org/) videos into Sphinx rst docs.

## Installation

Clone and cd into this repository, then:

```shell
pip install .
```

or install from PyPI:

```shell
pip install sphinxcontrib.asciinema
```

##  Usage

Append extension to sphinx `conf.py`:

```python
extensions = ['sphinxcontrib.asciinema']
```

Insert videos into `.rst` docs by embedding them from asciinema.org:

```rst
.. asciinema:: 261648
```

or for a local file with a self-hosted web player:

```rst
.. asciinema:: local_file.cast
```

It is possible to give options as well:

```rst
.. asciinema:: local_file.cast
   :preload: 1
   :theme: solarized-dark
```

You can enter all options from the [self-hosted player](https://github.com/asciinema/asciinema-player#asciinema-player-element-attributes)
and the [embedded asciinema.org player](https://asciinema.org/docs/embedding).

Default options can be set in `conf.py`:

```python
sphinxcontrib_asciinema_defaults = {
    'theme': 'solarized-dark',
    'preload': 1,
    'font-size': '15px'
}
```
