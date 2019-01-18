Python Microservice configuration module
-------------------------------------

[![CircleCI](https://circleci.com/gh/microparts/configuration-python/tree/master.svg?style=svg)](https://circleci.com/gh/microparts/configuration-python/tree/master)

Configuration module for microservices written on Python. Specially created
for follow up corporate standards of application configuration.

## Installation

```bash
pip3 install config_pkg
```

## Usage

By default path to configuration directory and application stage
loading from `/configuration` with `defaults` stage.

1) Simple
```python
from config_pkg import PKG

pkg = PKG()
pkg.load()

all_config = pkg.get_all()
foo_bar = pkg.get('foo.bar')
```

2) If u would like override default values, you can pass 2 arguments to
class constructor or set up use setters.

```python
from config_pkg import PKG

pkg = PKG('/configuration', 'test')
pkg.load()

foo_bar = pkg.get('key') # full example on the top
```

3) If the operating system has an env variables `CONFIG_PATH` and `STAGE`,
then values for the package will be taken from there.

```bash
export CONFIG_PATH=/configuration
export STAGE=test
```

```python
from config_pkg import PKG

pkg = PKG()
pkg.load() # loaded files from /configuration for prod stage.

foo_bar = pkg.get('key') # full example on the top
```

4) If u want to see logs and see how load process working,
pass you application logger to the following method:

```python
from config_pkg import PKG

pkg = PKG(logger=logger) # loggining.Logger compatible logger
pkg.load() 

foo_bar = pkg.get('key') # full example on the top
```

That all.

## Depends

* Python 3.x
* pip for install package

## License

MIT