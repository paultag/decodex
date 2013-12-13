from decodex import __appname__, __version__
from setuptools import setup


long_description = ""

setup(
    name=__appname__,
    version=__version__,
    scripts=[],
    packages=[
        'decodex',
        'decodex.decoders',
        'decodex.decoders.strings',
    ],
    author="Paul Tagliamonte",
    author_email="tag@pault.ag",
    long_description=long_description,
    description='decode codex codecs',
    license="AGPL3+",
    url="http://pault.ag/",
    platforms=['any'],
    entry_points={
        'console_scripts': [
            'decodex = decodex.cli:main',
        ],
    },
)
