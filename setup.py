#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu

from setuptools import setup

setup(name='py3compat',
      version='0.2',
      description='Small Python2/3 helpers to avoid depending on six.',
      long_description=("Based on Jinja2._compat module.\n"
                        "Some py2/py3 compatibility support based on a "
                        "stripped down version of six so we don't have "
                        "to depend on a specific version of it."),
      author='yeleman',
      author_email='rgaudin@gmail.com',
      url='http://github.com/yeleman/py3compat',
      py_modules=['py3compat'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
      ]
)
