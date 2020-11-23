#!/usr/bin/env python
from setuptools import find_packages, setup

setup(name='reduce_p',
      version='0.0.1',
      description='parallelized reduce for Python',
      author='IncubatorShokuhou',
      author_email='lh@lasg.iap.ac.cn',
      url='https://github.com/IncubatorShokuhou/reduce_p',
      license="GNU General Public License v3 (GPLv3)",
      install_requires=['more_itertools'],
      python_requires='>=3'
      )
