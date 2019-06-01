# -*- coding: utf-8 -*-

"""Main module."""
from .geohash_build import ffi
from .geohash_build import geohash_lib as lib


def geohash_encode(latitude: float, longitude: float, precision: int = -1):
    """Takes in latitude and longitude with a desired precision and returns the correct hash value.
    If precision < 0 or precision > 20, a default value of 6 will be used."""
    return ffi.string(lib.geohash_encode(latitude, longitude, precision)).decode()


def geohash_decode(hash_code: str):
    """Returns GeoCoord structure which contains the latitude and longitude
    that was decoded from the geohash. A GeoCoord also provides the bounding box for the
    geohash (north, east, south, west, dimension.height, dimension.width)."""
    return lib.geohash_decode(hash_code.encode())
