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
    os.path.join('syllable_samples/static/syllable_samples/', filename)
         for filename in os.listdir('syllable_samples/static/syllable_samples/')
]

print(audio_samples)

setup(
    name="syllable_samples",
    version="0.0.1",
    author="Jivan Amara",
    author_email="Development@JivanAmara.net",
    packages=['syllable_samples'],
    package_data={
        'syllable_samples': audio_samples,
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
