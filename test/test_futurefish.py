#!/bin/python

def test_coordinate_conversion:
    '''
    This will test that the Easting/Northing coordinate conversion to degrees
    lat/lon works correctly.
    '''
    known_easting, known_northing = 1779218.9152656617, -332620.1250442802
    known_latitude, known_longitude = 46.0845785270385, -118.30436442591215
    calculated_latitude, calculated_longitude = calcLatLon(known_easting,
                                                          known_northing)
    assertAlmostEqual(known_latitude, calculated_latitude)
    assertAlmostEqual(known_longitude, calculated_longitude)

def test_average_spatial:

def test_average_temporal:
