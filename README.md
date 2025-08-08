# Gravify

**Gravify** is a Python library to interface with Gravatar profiles and avatars.

```python
>>> from gravify import AvatarGenerator
>>> AvatarGenerator(size=500).generate_url('hello@example.com')
'https://gravatar.com/avatar/1753bdb368271a785887ddbfb926164f2f7c6a88f609c07ff0401c5572955206?s=500'
```

[![Total Downloads](https://img.shields.io/pepy/dt/gravify)][pypi]
[![Supported Versions](https://img.shields.io/pypi/pyversions/gravify.svg)][pypi]
[![Testing Status](https://img.shields.io/github/actions/workflow/status/bsoyka/gravify/test.yml?branch=main&label=tests)][testing]
[![Coverage](https://img.shields.io/codecov/c/github/bsoyka/gravify)][codecov]
[![GitHub last commit](https://img.shields.io/github/last-commit/bsoyka/gravify)][github]

## Installation and usage

Gravify is [available on PyPI][pypi].
Install it with your preferred package manager:

```sh
$ uv add gravify
$ pip install gravify
```

Gravify officially supports Python 3.10+.

**[Read the documentation][docs]** to learn how to use Gravify.

[codecov]: https://codecov.io/github/bsoyka/gravify

[docs]: https://gravify.readthedocs.io/

[github]: https://github.com/bsoyka/gravify

[license]: https://github.com/bsoyka/gravify/blob/master/LICENSE

[pypi]: https://pypi.org/project/gravify/

[testing]: https://github.com/bsoyka/gravify/actions/workflows/test.yml
