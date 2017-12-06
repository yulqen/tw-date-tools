from setuptools import setup, find_packages
import tw_holidays
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tw-holidays',
    version=tw_holidays.__version__,
    description='Get national holiday and convert it intwo taskwarrior rc format.',
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
        'tw-holidays = tw_holidays.main:main'
    ]},
    install_requires=['requests'],
    test_suite='tw_holidays.tests'
)
