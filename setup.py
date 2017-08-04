#!/usr/bin/env python

from setuptools import setup

setup(
    name='isatools',
    version='0.8.3',
    packages=['isatools', 'isatools.convert', 'isatools.io', 'isatools.net', 'isatools.create'],
    package_data={'isatools': ['resources/schemas/cedar/*.json',
                               'resources/schemas/isa_model_version_1_0_schemas/core/*.json',
                               'resources/schemas/configs/*.json',
                               'resources/schemas/configs/schemas/*.json',
                               'resources/config/json/default/*.json',
                               'resources/config/json/default/schemas/*.json',
                               'resources/config/json/sra/*.json',
                               'resources/config/json/sra/schemas/*.json',
                               'resources/config/xml/*.xml',
                               'resources/sra_schemas/*.xsd',
                               'resources/sra_templates/*.xml',
                               'resources/tab_templates/*.txt',
                               'net/resources/biocrates/*',
                               'net/resources/sra/*.xsl',
                               'net/resources/sra/*.xml'],
                  '': ['LICENSE.txt', 'README.md']},
    description='ISA-API',
    author='ISA Infrastructure Team',
    author_email='isatools@googlegroups.com',
    url='https://github.com/ISA-tools/isa-api',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        ],
    install_requires=[
        'numpy',
        'jsonschema',
        'pandas',
        'networkx',
        'lxml',
        'requests',
        'chardet',
        'iso8601',
        'jinja2',
        'bs4',
        'mzml2isa',
        'biopython',
        'progressbar2'
    ],
    test_suite='tests'
)
