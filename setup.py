from setuptools import setup
import os

# The absolute path to the directory containing this file
DIRPATH = os.path.dirname(os.path.abspath(__file__))
# allow setup.py to be run from any path
os.chdir(DIRPATH)

# README file
with open('README.rst', 'r') as rmf:
    README = rmf.read()

audio_samples = [
    os.path.join('static/syllable_samples/', filename)
         for filename in os.listdir('syllable_samples/static/syllable_samples/')
]

fixtures = [
    os.path.join('fixtures', filename) for filename in os.listdir('syllable_samples/fixtures/')
]

data_files = audio_samples + fixtures

setup(
    name="syllable_samples",
    version="0.1.0",
    author="Jivan Amara",
    author_email="Development@JivanAmara.net",
    packages=['syllable_samples', 'syllable_samples.migrations'],
    package_data={
        'syllable_samples': data_files,
    },
    description='Python library for recognizing the tone of a mandarin syllable',
    long_description=README,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
