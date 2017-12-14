#!/bin/python
import futurefish.data_processing as fd
import numpy as np
import pandas as pd
import unittest

class UnitTests(unittest.TestCase):
    def test_coordinate_conversion(self):
        """
        This will test that the Easting/Northing coordinate conversion to
        degrees lat/lon works correctly.
        """
        known_east, known_north = 1779218.9152656617, -332620.1250442802
        known_lat, known_long = 46.0845785270385, -118.30436442591215
        calculated_latitude, calculated_longitude = fd.calcLatLon(known_east,
                                                                  known_north)
        self.assertAlmostEqual(known_lat, calculated_latitude)
        self.assertAlmostEqual(known_long, calculated_longitude)


    def test_timeseries_processing(self):
        """
        This will test that the minimum seven day flow calculator works
        when applied to a sample dataset.
        """
        np.random.seed(0)
        sample_df = pd.DataFrame(np.random.rand(365*3)*10+2,
                                 index=pd.date_range('1989-01-01',
                                                     '1991-12-31'))
        known_mins = np.array([[4.27043629], [ 3.26292494], [ 4.48407596]])
        calc_mins = metric_min7day_streamflow(sample_df,
                                              slice('1989-01-01',
                                                    '1991-12-31')).values
        self.assertTrue(np.allclose(calc_mins, known_mins))
