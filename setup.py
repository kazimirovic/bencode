from setuptools import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='torrent-bencode',
    version='0.2',
    packages=['bencode'],
    url='https://github.com/kazimirovic/bencode',
    license='MIT',
    author='kazimirovic',
    author_email='kazimirovic@protonmail.com',
    description='An implementation of Bencode encoding in Python 3',
    long_description = readme
)
