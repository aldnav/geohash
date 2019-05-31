# -*- coding: utf-8 -*-

"""Main module."""
from .geohash_build import ffi
from .geohash_build import geohash_lib as lib


def geohash_encode(lat: float, long: float, precision: int):
    return ffi.string(lib.geohash_encode(lat, long, precision)).decode()


def geohash_decode(hash_code: str):
    return lib.geohash_decode(hash_code.encode())
