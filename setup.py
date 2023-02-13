import io
import os
import setuptools

here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

about = {}
with open(os.path.join(here, "sphinxcontrib", "asciinema", '__init__.py')) as f:
    exec(f.read(), about)

setuptools.setup(
    name="sphinxcontrib.asciinema",
    version=about['__version__'],
    packages=setuptools.find_packages(),
    install_requires=['sphinx'],
    include_package_data=True,
    license=about['__license__'],
    url='https://github.com/divi255/sphinxcontrib.asciinema',
    description='''Embed asciinema casts in your Sphinx docs''',
    long_description_content_type='text/markdown',
    long_description=long_description,
    namespace_packages=['sphinxcontrib'],
    classifiers='''
Framework :: Sphinx :: Extension
Programming Language :: Python
License :: OSI Approved :: MIT License
Programming Language :: Python :: 3
Topic :: Software Development :: Documentation
'''.strip().splitlines())
