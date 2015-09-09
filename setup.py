import re
from setuptools import setup, find_packages

versionPattern = re.compile(r"""^__version__ = ['"](.*?)['"]$""", re.M)
with open("fusion_util/_version.py", "rt") as f:
    version = versionPattern.search(f.read()).group(1)


setup(
    name='fusion-util',
    version=version,
    description='Utility package for Fusion',
    url='https://github.org/fusionapp/fusion-util',
    install_requires=[
        'Twisted[tls] >= 15.0.0',
        'txspinneret >= 0.1.2',
        'testtools',
        ],
    license='MIT',
    packages=find_packages(),
    include_package_data=True)
