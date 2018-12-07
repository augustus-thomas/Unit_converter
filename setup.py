#!/usr/bin/env python
# Work around mbcs bug in distutils.
# http://bugs.python.org/issue10945
import codecs
try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    func = lambda name, enc=ascii: {True: enc}.get(name=='mbcs')
    codecs.register(func)
from distutils.core import setup

setup(name='Unit Converter',
      version='1.0',
      description='Python Distribution Utilities',
      author='Jesse MacFarlane Thomas',
      author_email='jessemacfarlane@gmail.com ',
      packages=['Unit_converter'],
      package_data={'Unit_converter':['ESP_logo.png']},
      package_dir={'Unit_converter':'.'}
     )