# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from __future__ import absolute_import

import os

from setuptools import find_packages
from setuptools import setup

here = os.path.dirname(__file__)

setup(
    name='releng_slavehealth',
    version=open(os.path.join(here, 'VERSION')).read().strip(),
    description='The code behind https://slavehealth.mozilla-releng.net/',
    author='Rok Garbas',
    author_email='garbas@mozilla.com',
    url='https://slavehealth.mozilla-releng.net',
    tests_require=[
        'flake8',
        'pytest',
    ],
    install_requires=[
        'releng_common[log,api,cors,auth,db]',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    license='MPL2',
)
