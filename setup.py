"""
distutils setup script used to build, install and test the included packages

for info on how to write the script read:
    https://docs.python.org/2/distutils/setupscript.html

"""
import os
import sys
from setuptools import setup, find_packages

import config

# ROOT path
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

# project version
version = config.get_project_version()

# extra keyword arguments
extra_kwargs = {}
if sys.version_info >= (3,):
    # python 3
    extra_kwargs['use_2to3'] = True

# test requirements
tests_require = ['mock']
if sys.version_info < (2, 7):
    tests_require.append('unittest2')
tests_require = tests_require + config.get_test_requirements()

# install requirements
requirements_file = os.path.join(ROOT_PATH, 'requirements.txt')
try:
    install_requires = [
        x.strip() for x in open(requirements_file).read().split('\n') if x
    ]
except IOError:
    sys.stderr.write(
        "[ERROR] Cannot find file specified as "
        "``install requirements`` (%s)\n" % requirements_file
    )
    sys.exit(1)

exclude_packages = config.get_exclude_packages()
packages = [x for x in find_packages() if x not in exclude_packages]

setup(
    name=config.get_project_name(),         # name of your app
    version=version,
    license=config.get_project_license(),  # license

    # test configuration
    test_suite=config.get_test_suite(),
    tests_require=tests_require,

    # install configuration
    install_requires=install_requires,

    # your app description
    description=config.get_project_desc(),
    long_description=open('README.md').read(),

    # author info
    author=config.get_author_name(),
    author_email=config.get_author_email(),

    # app location
    url=config.get_project_url(),
    download_url=config.get_project_download_url(),

    # packages
    packages=packages,
    include_package_data=True,

    zip_safe=False,

    # for a list of valid classifiers see:
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
