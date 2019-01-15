#   Copyright 2017-18 Soroco Americas Private Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#   Primary Author: George Nychis <george@soroco.com>
#
#   Purpose: Make this library publishable to PyPI.  This file is a modified
#   version of
#   https://raw.githubusercontent.com/pypa/sampleproject/master/setup.py.
"""
This provides support around the migration of a single project and backlog to
Azure DevOps and its native work item types for User Story, Tasks, and Bugs.
"""


from codecs import open
from os import path
from setuptools import setup, find_packages


from pyce import __version__


# Get the long description from the README file
HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    author='Soroco Americas Private Limited',  # Optional
    author_email='opensource@soroco.com',  # Optional
    classifiers=[  # Optional
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
    ],
    description='Migration of projects from Gitlab to Azure DevOps.',  # Required
    install_requires=['vsts==0.1.25', 'python-gitlab==1.7.0', 'markdown==3.0.1',
        'markdown2==2.3.7', 'bs4==0.0.1'],  # Optional
    keywords='gitlab azure devops microsoft',  # Optional
    license='Apache Software License Version 2.0',  # Optional
    long_description=LONG_DESCRIPTION,  # Optional
    long_description_content_type="text/markdown",  # Optional
    maintainer='Soroco Americas Private Limited',  # Optional
    maintainer_email='opensource@soroco.com',  # Optional
    name='gladops-migration',  # Required
    platforms=['Windows 10', 'Windows Server 2008', 'Windows Server 2012',
               'Linux'],  # Optional
    packages=find_packages(exclude=[]),  # Required
    python_requires='>=3.6, <3.8',
    url='https://github.com/soroco/gladops-migration',  # Optional
    version=__version__,  # Required
)
