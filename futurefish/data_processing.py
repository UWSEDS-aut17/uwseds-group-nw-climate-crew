def calcLatLon(northing, easting):
    '''
    This function converts northings/eastings to latitude and longitudes.
    It is almost entirely based upon a function
    written by Tom Neer found in November 2017 at his blog:
    http://www.neercartography.com/convert-consus-albers-to-wgs84/
    '''
    from math import asin, atan2, cos, log, pow, sin, sqrt

    # CONSUS Albers variables (EPSG: 5070)
    RE_NAD83 = 6378137.0
    E_NAD83 = 0.0818187034  #Eccentricity
    D2R = 0.01745329251     #Pi/180
    standardParallel1 = 43.
    standardParallel2 = 47.
    centralMeridian = -114.
    originLat = 30
    originLon = 0

    m1 = cos(standardParallel1 * D2R)/ \
         sqrt(1.0 - pow((E_NAD83 * sin(standardParallel1 * D2R)), 2.0))
    m2 = cos(standardParallel2 * D2R)/ \
         sqrt(1.0 - pow((E_NAD83 * sin(standardParallel2 * D2R)), 2.0))

    def calcPhi(i):
        sinPhi = sin(i * D2R)
        return (1.0 - pow(E_NAD83, 2.0)) \
               * ((sinPhi/(1.0 - pow((E_NAD83 * sinPhi), 2.0))) \
               - 1.0/(2.0 * E_NAD83) \
               * log((1.0 - E_NAD83 * sinPhi)/(1.0 + E_NAD83 * sinPhi)))

    q0 = calcPhi(originLat)
    q1 = calcPhi(standardParallel1)
    q2 = calcPhi(standardParallel2)
    nc = (pow(m1, 2.0) - pow(m2, 2.0)) / (q2 - q1)
    C = pow(m1, 2.0) + nc * q1
    rho0 = RE_NAD83 * sqrt(C - nc * q0) / nc
    rho = sqrt(pow(easting, 2.0) + pow((rho0 - northing), 2.0))
    q = (C - pow((rho * nc / RE_NAD83), 2.0)) / nc
    beta = asin(q / (1.0 - log((1.0 - E_NAD83) / (1.0 + E_NAD83)) * (1.0 - pow(E_NAD83, 2.0))/(2.0 * E_NAD83)))
    a = 1.0 / 3.0 * pow(E_NAD83, 2.0) + 31.0 / 180.0 * pow(E_NAD83, 4.0) + 517.0 / 5040.0 * pow(E_NAD83, 6.0)
    b = 23.0/360.0 * pow(E_NAD83, 4.0) + 251.0 / 3780.0 * pow(E_NAD83, 6.0)
    c = 761.0/45360.0 * pow(E_NAD83, 6.0)
    theta = atan2(easting, (rho0 - northing))

    lat = (beta + a * sin(2.0 * beta) + b * sin(4.0 * beta) + c * sin(6.0 * beta))/D2R
    lon = centralMeridian + (theta / D2R) / nc
    coords = [lat, lon]

    return coords


def get_model_ts(infilename, na_values='-9999', comment='#',
                 rename_columns=None, column='streamflow'):
    '''Retrieve modeled time series from ASCII file
    Parameters
    ----------
    infilename : str
        Pathname for file
    na_values : str, optional
        Values that should be converted to `NA`. Default value is '-9999'
    comment : str, optional
        Comment indicator at the start of the line. Default value is '#'=
    rename_columns: dict or None, optional
        Dictionary to rename columns. Default value is None
    column = str, optional
        Name of the column that will be returned. Default value is 'streamflow'
    Returns
    -------
    pandas.Series
        Column from file as a pandas.Series
    '''
    ts = pd.read_csv(infilename, comment=comment, na_values=na_values,
                     index_col=0, parse_dates=True)
    # renaming of columns may seem superfluous if we are converting to a Series
    # anyway, but it allows all the Series to have the same name
    if rename_columns:
        ts.columns = [column]
    return pd.Series(ts[column])


def locate_nearest_neighbor_values(point, gdf, temperature_sites):
    tree = KDTree(temperature_sites, leafsize=temperature_sites.shape[0]+1)
    distances, ndx = tree.query([point], k=10)
    nearest_neighbors_data = gdf.iloc[list(ndx[0])]
    return nearest_neighbors_data
