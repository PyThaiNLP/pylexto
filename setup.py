# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages
import sys
requirements = [
    'JPype1',
    'future>=0.16.0'
]
test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pylexto',
    version='1.0',
    description="LexTo with Python 2 & 3 Wrapper",
    author='Wannaphong Phatthiyaphaibun',
    author_email='wannaphong@yahoo.com',
    url='https://github.com/wannaphongcom/pylexto/',
    packages=find_packages(),
    package_data={'pylexto':['lexitron.txt'],'pylexto.LongLexTo':['license.txt','LongLexTo.class','LongLexTo.java','LongParseTree.class','LongParseTree.java','Trie.class','Trie.java']},
    include_package_data=True,
    install_requires=requirements,
    license='MIT',
    zip_safe=False,
    keywords='pylexto',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: Thai',
        'Topic :: Text Processing :: Linguistic',
        'Programming Language :: Python :: Implementation'],
)
