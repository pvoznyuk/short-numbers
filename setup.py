from distutils.core import setup
from shortnumbers.shortnumbers import __version__, __author__

setup(
    name='shortnumbers',
    packages=['shortnumbers'],
    version=__version__,
    description='A Python package to display big numbers in short format and vice-versa',
    author=__author__,
    author_email='pavlo.vozniuk@gmail.com',
    url='https://github.com/pvoznyuk/short-numbers',
    download_url = 'https://github.com/pvoznyuk/short-numbers/archive/' + __version__ + '.tar.gz',
    keywords = ['numbers', 'formatting', 'parse'],
    classifiers = []
)
