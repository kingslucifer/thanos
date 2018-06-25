# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 14:49:41 2018

@author: zy259
"""
from setuptools import setup, find_packages

setup(
      name='thanos',
      version='1.0',
      packages=find_packages(),
      description='thanos models and migration with Alembic',
      install_requires=[
              "alembic>=0.9.5",
              "psycopg2>=2.7.3",
              "SQLALchemy>=1.1.17"
      ],
      python_requires='>=3.5'
      )