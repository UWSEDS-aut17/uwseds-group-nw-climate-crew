# Component Design 

**1. Reading data:**
This is necessary in order to access the information.
**2. Processing data:**
This is necessary to get our data in the right format.
**3. Determining future projections:**
This will run a simple model to link the data uploaded and processed in steps 1 and 2. It is necessary for use cases 2 and 3 in our functional specifications.
**4. Mapping/visualizing data:**
This will allow us to share the results in an interactive format. This is necessary for all use cases.
**5. User interface:** This will let the user interact with the data and get answers to their questions.

### 1. Reading data:   
There are three datasets to import for this project: 
* Stream flow data (.csv file): this data can be found at http://hydro.washington.edu/crcc/. The variables we'll use from this dataset are: 
	* day from 1950 through 2099
	* daily average streamflow (cubic feet per second)
* Stream flow temperatures (.csv file): this data can be found at https://www.fs.fed.us/rm/boise/AWAE/projects/NorWeST.html#downloads. The variables in this dataset that we will use are:
	* location
	* date
	* daily max and min
	* daily mean and standard deviation 
* Salmon species spawning location (table in paper, which is need to be manually input as a .csv file). The variables in this dataset that we will use are: 
	* Salmon specie
	* Spawning river
	 
This component will load the .csv files using pandas.read_csv and build a pandas dataframe (for all three datasets)

### 2. Processing data: 
This is necessary to get our data in the right format. For example, calculating annual averages or other basic statistics.
- This function takes the data read in in step 1 and puts it in format usable by step 3.
- Name of the fuction: process_data
- inputs: the complete timeseries output from step 1; these will be daily mean temperature and streamflow at sites throughout the domain within the critical periods for each salmon species. 
- outputs: a projection (categorical on a scale of 1 to 5) for salmon survival within a given time frame for each site in the domain.


### 3. Determining future projections:
This will run a simple model to link the data uploaded and processed in steps 1 and 2. It is necessary for use cases 2 and 3 in our functional specifications. 



### 4. Mapping/visualizing data:
This will allow us to share the results in an interactive format. This is necessary for all use cases. 

### 5. User interface:
This will let the user interact with the data and get answers to their questions.
