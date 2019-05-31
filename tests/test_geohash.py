#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `geohash` package."""

import pytest
from geohash import geohash

geohash_map = (
    ((35.689487, 139.691706), "xn774c"),
    ((35.179554, 129.075642), "wy7b1h"),
    ((48.856614, 2.352222), "u09tvw"),
)


@pytest.mark.parametrize("coordinates, expected", geohash_map)
def test_geohash_encode(coordinates, expected):
    lat, long = coordinates
    # precision >= 0 then precision = 12
    assert geohash.geohash_encode(lat, long, -1) == expected


@pytest.mark.parametrize("expected, hash_code", geohash_map)
def test_geohash_decode(hash_code, expected):
    location = geohash.geohash_decode(hash_code)
    assert all(
        [
            location.longitude,
            location.latitude,
            location.north,
            location.east,
            location.south,
            location.west,
            location.dimension,
        ]
    )
