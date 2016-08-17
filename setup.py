#!/usr/bin/env python

from distutils.core import setup
from jsoninspectlib import __version__

setup(
    name = 'json-inspect',
    version = __version__,

    author = 'John Murray',
    author_email = 'me@johnmurray.io',
    description = 'JSON inspection command line client',
    license='Apache 2.0',
    packages = ['jsoninspectlib'],
    scripts = ['json-inspect'],
    url = 'http://github.com/JohnMurray/json-inspect',
 )
