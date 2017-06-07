try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A producer-consumer example using web-sockets',
    'author': 'Corigan Simpson',
    'url': '',
    'author_email': 'corigansimpson@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['consumer', 'producer'],
    'scripts': [],
    'name': 'web-sockets_concurrency'
}

setup(**config)
