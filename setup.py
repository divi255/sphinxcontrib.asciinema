import setuptools
from sphinxcontrib import asciinema as pkg

pkgname = pkg.__name__

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name=pkgname,
    version=pkg.__version__,
    packages=setuptools.find_packages(),
    install_requires=['sphinx'],
    include_package_data=True,
    license=pkg.__license__,
    url='https://github.com/teake/sphinxcontrib.asciinema',
    description='''embedding asciinema videos in Sphinx docs''',
    long_description_content_type='text/markdown',
    long_description=long_description,
    namespace_packages=['sphinxcontrib'],
    classifiers='''
Programming Language :: Python
License :: OSI Approved :: MIT License
Programming Language :: Python :: 3
Topic :: Software Development :: Documentation
'''.strip().splitlines())
