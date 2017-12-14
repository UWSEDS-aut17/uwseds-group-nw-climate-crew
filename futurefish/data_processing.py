def calcPhi(i, D2R, sinPhi, E_NAD83):
    '''
    This funciton takes as input a latitude and then returns a phi value to be
    used in the further calculation of the converted coordinates.
    '''
    sinPhi = sin(i * D2R)
    final_phi = (
                 (1.0 - pow(E_NAD83, 2.0)) * ((sinPhi/(1.0 - pow((E_NAD83 *
                 sinPhi), 2.0))) - 1.0/(2.0 * E_NAD83) * log((1.0 - E_NAD83 *
                 sinPhi)/(1.0 + E_NAD83 * sinPhi)))
                )

    return final_phi


def calcLatLon(northing, easting):
    '''
    This function converts northings/eastings to latitudes and longitudes.
    It is almost entirely based upon a function written by Tom Neer accessed by
    the futurefish developers in November 2017 at his blog:
    http://www.neercartography.com/convert-consus-albers-to-wgs84/
    The main changes to the function were to add documentation where it was
    helpful and also to change the central meridian and standard parallel to
    coordinates appropriate for the domain of the Pacific Northwest.
    '''
    from math import asin, atan2, cos, log, pow, sin, sqrt

    # CONUS Albers variables (EPSG: 5070)
    # These variables are prescribed in the definition of the Albers projection
    RE_NAD83 = 6378137.0
    # Eccentricity
    E_NAD83 = 0.0818187034
    # Pi/180
    D2R = 0.01745329251
    standardParallel1 = 43.
    standardParallel2 = 47.
    centralMeridian = -114.
    originLat = 30
    originLon = 0

    # Below there is a long string of calculations involving converting
    # geocoordinates.
    m1 = cos(standardParallel1 * D2R)/sqrt(1.0 - pow((E_NAD83 *
            sin(standardParallel1 * D2R)), 2.0))
    m2 = cos(standardParallel2 * D2R)/sqrt(1.0 - pow((E_NAD83 *
            sin(standardParallel2 * D2R)), 2.0))
    q0 = calcPhi(originLat, D2R, sinPhi, E_NAD83)
    q1 = calcPhi(standardParallel1, D2R, sinPhi, E_NAD83)
    q2 = calcPhi(standardParallel2, D2R, sinPhi, E_NAD83)
    nc = (pow(m1, 2.0) - pow(m2, 2.0)) / (q2 - q1)
    C = pow(m1, 2.0) + nc * q1
    rho0 = RE_NAD83 * sqrt(C - nc * q0) / nc
    rho = sqrt(pow(easting, 2.0) + pow((rho0 - northing), 2.0))
    q = (C - pow((rho * nc / RE_NAD83), 2.0)) / nc
    beta = (
            asin(q / (1.0 - log((1.0 - E_NAD83) / (1.0 + E_NAD83)) * (1.0 -
            pow(E_NAD83, 2.0))/(2.0 * E_NAD83)))
            )
    a = (
         1.0 / 3.0 * pow(E_NAD83, 2.0) + 31.0 / 180.0 * pow(E_NAD83, 4.0) +
         517.0 / 5040.0 * pow(E_NAD83, 6.0)
        )
    b = 23.0/360.0 * pow(E_NAD83, 4.0) + 251.0 / 3780.0 * pow(E_NAD83, 6.0)
    c = 761.0/45360.0 * pow(E_NAD83, 6.0)
    theta = atan2(easting, (rho0 - northing))

    lat = (beta + a * sin(2.0 * beta) + b * sin(4.0 * beta) + c * sin(6.0 *
            beta))/D2R
    lon = centralMeridian + (theta / D2R) / nc
    coords = [lat, lon]

    return coords


def convert_coordinates(gdf, false_easting):
    '''
    This function reads a geodataframe, extracts the coordinates from it
    and then converts those from Albers eastings/northings into
    latitude/longitude coordinates. It needs a false easting as one of the
    input parameters. This is specified by the projection within the
    geodataframe but is not always included in the metadata and so
    we allow for it to be specified manually.

    Parameters
    -----------
    gdf : geopandas dataframe
    false_easting : float
    '''
    # Initialize your list of latitudes and longitudes
    lat_lons = []
    for (i, point) in enumerate(cleaned_up_gdf.geometry[:]):
        # The false easting is from streamflow temperature
        # dataset documentation within the GIS shapefile
        northing = point.coords.xy[1][0]
        easting = point.coords.xy[0][0] - false_easting
        [lat, lon] = calcLatLon(northing, easting)
        lat_lons.append([lat, lon])
    temperature_sites = np.array(lat_lons)
    return temperature_sites

def create_collated_dataset_temperature(translating_temperature_keys_dictionary,
                           streamflow_sites,
                           cleaned_up_gdf_future,
                           cleaned_up_gdf_historical)
    '''
    This function creates a dataframe with the stream temperature
    estimates. It will be later populated by streamflow projections
    by later processing steps.

    Parameters
    ----------
    translating_temperature_keys_dictionary : dict
        Dictionary that translates the somewhat obfuscated column names
        from the convention of the temperature dataset into meaningful
        column names.

    streamflow_sites : pandas DataFrame
        The object with all of the information about the
        streamflow locations' coordinates and their IDs. It is used to
        link the streamflow sites to the stream temperature sites
        geographically

    cleaned_up_gdf_future: geopandas dataframe
        Dataframe with future streamflow temperature projections.

    cleaned_up_gdf_historical: geopandas dataframe
        Dataframe with historical streamflow temperature projections.
    '''

    collated_dataset = pd.DataFrame(index=streamflow_sites['Site ID'],
        columns=list(translating_temperature_keys_dictionary.values()))
    for site in streamflow_sites['Site ID']:
    # Loop through each location in the streamflow set and
    # select the 10 nearest points within the stream temperature set
        point = [streamflow_sites[streamflow_sites['Site ID']==
                 site]['Latitude'].values[0],
                 streamflow_sites[streamflow_sites['Site ID']==
                 site]['Longitude'].values[0]]
        locate_nearest_neighbor_values(point, cleaned_up_gdf,
                                       temperature_sites, 10)

    # First set the future time periods' data
        for variable in ['S39_2040DM', 'S41_2080DM']:
            collated_dataset.set_value(site,
                            translating_temperature_keys_dictionary[variable],
                            nearest_neighbors_data_future[variable].mean())

    # Then set the historic values
        nearest_neighbors_data_historical =
                                cleaned_up_gdf_historical.iloc[list(ndx[0])]

        collated_dataset.set_value(site,
                    'Stream Temperature Historical',
                    nearest_neighbors_data_historical['Historical'].mean())
        return collated_dataset

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


def locate_nearest_neighbor_values(point, gdf, sites,
                                   number_of_nearest_neighbors):
    '''
    This function takes geopandas information as inputs as well as
    latitude/longitude coordinates of locations and returns the nearest
    neighbors present in the geodataframe.
    Parameters
    ----------
    point : list
        List of latitude/longitude coordinates
    gdf : geopandas geodataframe
        Geospatial information
    sites : numpy array
        Array with list of coordinates
    number_of_nearest_neighbors : int
        The number of nearest neighbors you want to return
    '''
    # Create your nearest neighbor mapping
    tree = KDTree(sites, leafsize=sites.shape[0]+1)

    # Calculate distances and indices involving nearest neighbors
    distances, ndx = tree.query([point], k=number_of_nearest_neighbors)

    # Access the appropriate nearest neighbors within the geodataframe
    nearest_neighbors_data = gdf.iloc[list(ndx[0])]

    return nearest_neighbors_data
