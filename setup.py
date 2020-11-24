#!/usr/bin/env python
from setuptools import find_packages, setup,find_namespace_packages

setup(name='reduce_p',
      version='0.0.2',
      description='parallelized reduce for Python',
      author='Hao Lyu',
      author_email='lh@lasg.iap.ac.cn',
      url='https://github.com/IncubatorShokuhou/reduce_p',
      license="GNU General Public License v3 (GPLv3)",
      install_requires=['more_itertools'],
      python_requires='>=3',
      # packages=find_packages(exclude=['contrib', 'docs', 'tests*'])
      packages = find_namespace_packages()
      )
