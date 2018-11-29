from setuptools import setup, find_packages

__version__ = '1.0.0'

setup(
    version=__version__,
    name='config_pkg',
    packages=find_packages(),

    install_requires=[
        'pyyaml'
    ],

    description='Python Config PKG',

    author='Roquie, detrous',
    author_email='roquie0@gmail.com, artyom.slobodyan@gmail.com',

    url='https://github.com/microparts/configuration-python',
    download_url='https://github.com/microparts/configuration-python/archive/%s.tar.gz' % __version__,

    license='GPL-3.0-only',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL-3.0-only',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)