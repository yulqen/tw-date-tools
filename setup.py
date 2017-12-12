from setuptools import setup, find_packages
import tdt
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tw-date-tools',
    version=tdt.__version__,
    description='Process date and holiday data in taskwarrior.',
    long_description=long_description,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Other Audience",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Text Processing",
    ],
    keywords='data console commandline taskwarrior dates',
    author='Matthew Lemon',
    author_email='matt@matthewlemon.com',
    maintainer='Matthew Lemon',
    maintainer_email='matt@matthewlemon.com',
    url='',
    license='MIT',
    packages=find_packages(),
    python_requires='>=3.6',
    entry_points={'console_scripts': [
        'tdt = tdt.main:main'
    ]},
    install_requires=['requests'],
    test_suite='tdt.tests'
)
