__version__ = "0.1.1"

import setuptools
from sphinxcontrib import asciinema as pkg

pkgname = pkg.__name__

setuptools.setup(
    name=pkgname,
    version=pkg.__version__,
    packages=setuptools.find_packages(),
    install_requires=['sphinx'],
    author=pkg.__author__,
    license=pkg.__license__,
    url='https://github.com/divi255/sphinxcontrib.asciinema',
    description='''embedding asciinema videos in Sphinx docs''',
    long_description=pkg.__doc__,
    namespace_packages=['sphinxcontrib'],
    classifiers='''
Programming Language :: Python
License :: OSI Approved :: MIT License
Programming Language :: Python :: 3
Topic :: Software Development :: Documentation
'''.strip().splitlines())
