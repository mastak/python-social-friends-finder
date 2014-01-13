# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='python-social-friends-finder',
    version='0.1',
    author=u'Lubimov Igor',
    author_email='infunt@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/mastak/python-social-friends-finder.git',
    license='BSD licence, see LICENCE.txt',
    description='An extension app for python-social-auth that fetches your friends from different social-networks.',
    long_description=open('README.md').read(),
    zip_safe=False,
)
