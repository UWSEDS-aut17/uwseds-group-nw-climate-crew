from __future__ import absolute_import, division, print_function
from os.path import join as pjoin

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
_version_major = 0
_version_minor = 0
_version_micro = ''  # use '' for first of series, number for 1 and above
_version_extra = 'dev'
# _version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = '.'.join(map(str, _ver))

CLASSIFIERS = ["Development Status :: 0 - Alpha",
               "Environment :: Web",
               "Intended Audience :: Educational",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Fish"]

# Description should be a one-liner:
description = "futurefish: an interactive fish viability dashboard"
# Long description will go up on the pypi page
long_description = """

FutureFish
==========
FutureFish is a application with an interactive map that allows users
to see how climat change may affect salmon populations into the 21st 
century. 

To get started, please go to the
repository README_.

.. _README: https://github.com/UWSEDS-aut17/uwseds-group-nw-climate-crew/blob/master/README.md

License
=======
``futurefish`` is licensed under the terms of the MIT license. See the file
"LICENSE" for information on the history of this software, terms & conditions
for usage, and a DISCLAIMER OF ALL WARRANTIES.

All trademarks referenced herein are property of their respective holders.

Copyright (c) 2017 -, Andrew Bennett, Katie Brennan,
Oriana Chegwidden, Jennifer Hsiao, Serena Liu
"""

NAME = "futurefish"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "http://github.com/UWSEDS-aut17/uwseds-group-nw-climate-crew"
DOWNLOAD_URL = ""
LICENSE = "MIT"
PLATFORMS = "OS Independent"
AUTHOR = ('Andrew Bennett, Katie Brennan, Oriana Chegwidden, '
          'Jennifer Hsiao,  Serena Liu'),
MAJOR = _version_major
MINOR = _version_minor
MICRO = _version_micro
VERSION = __version__
PACKAGE_DATA = {'futurefish': [pjoin('data', '*')]}
REQUIRES = ['numpy', 'scipy', 'matplotlib', 'dash',
            'pandas', 'plotly', 'geopandas', 'dash_renderer',
            'dash_html_components', 'dash_core_components']
