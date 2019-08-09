sphinxcontrib-asciinema
***********************

Easily embed [asciinema](https://asciinema.org/) videos into Sphinx rst docs.

Installation
============

```shell
pip3 install sphinxcontrib.asciinema
```

Usage
=====

Append extension to sphinx *conf.py*:

```python
extensions = ['sphinxcontrib.asciinema']
```

Insert videos into *rst* docs:

```rst
.. asciinema:: 261648
```

or

```rst
.. asciinema:: https://asciinema.org/a/26148
```

(replace "261648" with your video id)

Enjoy!
