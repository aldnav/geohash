=====
Usage
=====

To use Geohash in a project::

    import geohash

* Encode::

    # Get geohash given latitude and longitude. Precision is optional.
    geohash.geohash_encode(latitude=48.856614, longitude=2.352222, precision=6)
    >> u09tvw

  Takes in latitude and longitude with a desired precision and returns the correct hash value. If precision < 0 or
  precision > 20, a default value of 6 will be used.

* Decode::

    # Get latitude, longitude and information about bounding box too!
    korea = geohash.geohash_decode(hash_code="wy7b1h")
    korea.latitude
    korea.longitude
    korea.north, korea.east, korea.south, korea.west
    korea.dimension.height, korea.dimension.width

  Returns GeoCoord structure which contains the latitude and longitude that was decoded from the geohash.
  A GeoCoord also provides the bounding box for the geohash.
