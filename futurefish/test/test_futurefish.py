#!/bin/python


def test_coordinate_conversion():
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


def test_timeseries_processing():
    '''
    This will test that the minimum seven day flow calculator works when
    applied to a sample dataset.
    '''
    np.random.seed(0)
    sample_df = pd.DataFrame(np.random.rand(365*3)*10+2,
                            index=pd.date_range('1989-01-01', '1991-12-31'))
    known_minimums = np.array([[4.27043629], [ 3.26292494], [ 4.48407596]])
    calculated_minimums = metric_min7day_streamflow(sample_df,
                                slice('1989-01-01', '1991-12-31')).values
    assert(np.allclose(calculated_minimums, known_minimums))
