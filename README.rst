=======
Geohash
=======


.. image:: https://img.shields.io/pypi/v/geohash.svg
        :target: https://pypi.python.org/pypi/geohash

.. image:: https://img.shields.io/travis/aldnav/geohash.svg
        :target: https://travis-ci.org/aldnav/geohash

.. image:: https://readthedocs.org/projects/geohash/badge/?version=latest
        :target: https://geohash.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Encode/decode Geohashes http://geohash.org

Wraps Derek Smith `libgeohash`. See https://github.com/simplegeo/libgeohash for implementation.


* Free software: GNU General Public License v3
* Documentation: https://geohash.readthedocs.io.


Features
--------

* Encode

.. code-block:: python

    print(geohash_encode(35.689487, 139.691706))
    # xn774c <- hash for Tokyo, Japan

* Decode

.. code-block:: python

    paris = geohash_decode('u09tvw')
    print(paris.latitude, paris.longitude)
    # 48.856614, 2.352222

Credits
-------

Geohash implementation is by Derek Smith's `libgeohash`. See https://github.com/simplegeo/libgeohash

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
