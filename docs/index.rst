Gravify
=======

**Gravify** is a Python library to interface with Gravatar profiles and avatars.

>>> from gravify import AvatarGenerator
>>> AvatarGenerator(size=500).generate_url('hello@example.com')
'https://gravatar.com/avatar/1753bdb368271a785887ddbfb926164f2f7c6a88f609c07ff0401c5572955206?s=500'

|Total Downloads| |Supported Versions| |Testing Status| |Coverage| |GitHub last commit| |GitHub Repo stars|

.. |Total Downloads| image:: https://img.shields.io/pepy/dt/gravify
   :target: https://pypi.org/project/gravify/
   :alt: Total Downloads

.. |Supported Versions| image:: https://img.shields.io/pypi/pyversions/gravify.svg
   :target: https://pypi.org/project/gravify/
   :alt: Supported Versions

.. |Testing Status| image:: https://img.shields.io/github/actions/workflow/status/bsoyka/gravify/test.yml?branch=main&label=tests
   :target: https://github.com/bsoyka/gravify/actions/workflows/test.yml
   :alt: Testing Status

.. |Coverage| image:: https://img.shields.io/codecov/c/github/bsoyka/gravify
   :target: https://codecov.io/github/bsoyka/gravify
   :alt: Coverage

.. |GitHub last commit| image:: https://img.shields.io/github/last-commit/bsoyka/gravify
   :target: https://github.com/bsoyka/gravify
   :alt: GitHub last commit

.. |GitHub Repo stars| image:: https://img.shields.io/github/stars/bsoyka/gravify
   :target: https://github.com/bsoyka/gravify
   :alt: GitHub Repo stars

Installation
------------

Gravify is `available on PyPI <https://pypi.org/project/gravify/>`_.
Install it with your preferred package manager:

.. code-block:: shell

    $ uv add gravify
    $ pip install gravify

Gravify officially supports Python 3.9+.

Tutorials and examples
----------------------
.. toctree::
    :maxdepth: 2

    tutorials/avatars
    tutorials/profiles

Further reference
-----------------
.. toctree::
    :maxdepth: 3

    reference/avatars
    reference/profiles
