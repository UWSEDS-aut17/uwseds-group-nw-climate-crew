#!/usr/bin/env python

import sys
try:
    from setuptools import setup
except:
    from distutils.core import setup

if sys.version_info.major != 3:
    print('-----------------------------------------')
    print('  ERROR: Future Fish requires Python 3!')
    print('-----------------------------------------')
    exit(1)


opts = dict(name='futurefish',
            description='Dashboard for climate projection impact on NW fish',
            url='',
            version='0.0.1',
            packages=['futurefish'],
            package_data = {'futurefish': [pjoin('data', '*')]
            scripts=['scripts/futurefish_dash.py'],
            install_requires=['numpy',
                              'pandas',
                              'plotly',
                              'geopandas',
                              'dash',
                              'dash-renderer',
                              'dash-html-components',
                              'dash-core-components'
                              ]
            )


if __name__ == '__main__':
    setup(**opts)
