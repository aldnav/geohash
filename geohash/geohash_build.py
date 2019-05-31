from pathlib import Path

from cffi import FFI

ffi = FFI()
ffi.cdef(
    """
    // Metric in meters
    typedef struct GeoBoxDimensionStruct {
        
        double height;
        double width;
    
    } GeoBoxDimension;
    
    typedef struct GeoCoordStruct {
        
        double latitude;
        double longitude;
        
        double north;
        double east;
        double south;
        double west;
    
        GeoBoxDimension dimension;
        
    } GeoCoord;


    char* geohash_encode(double lat, double lng, int precision);
    GeoCoord geohash_decode(char* hash);
"""
)
_geohash_lib_path = Path(__file__).parent / "bin/linux/geohash.so"
geohash_lib = ffi.dlopen(str(_geohash_lib_path.absolute()))
ffi.set_source("_geohash", None)
