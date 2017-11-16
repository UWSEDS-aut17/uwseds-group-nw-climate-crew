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

-----

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
* Salmon species spawning location (table in paper, which needs to be manually input as a .csv file). The variables in this dataset that we will use are:
	* Salmon species
	* Spawning river

This component (function named import_data)  will load the .csv files using pandas.read_csv and build a pandas dataframe (for all three datasets)

-----

### 2. Processing data:
This is necessary to get our data in the right format. For example, calculating annual averages or other basic statistics.
- This function takes the data read in in step 1 and puts it in format usable by step 3.
- Name of the fuction: process_data
- inputs: the complete timeseries output from step 1
- outputs: basic statistics conducted upon the inputs. For example, minimum streamflow calculated at sites throughout the domain within the critical periods for each salmon species.

-----

### 3. Determining future projections:
This component  will run a simple model to predict salmon populations based on forecasted stream temperature and stream flow data:
* predict_salmon_pop: predicts salmon population based on stream temperature and flow rate. Input: temperature (float), flow rate (float), and salmon species (factor). Output: predicted salmon population (float)
* generate_predictions: takes full set of input data and predicts salmon populations for all timepoints. Input: temperature data (dataframe of float values; rows correspond to timepoints, columns correspond to locations), flow rate data (dataframe of float values; rows are timepoints, columns are locations), salmon species (factor). Output: dataframe of predicted salmon populations for the given species (float; rows correspond to timepoints, columns correspond to locations).

-----

### 4. Mapping/visualizing data:
This will allow us to display the results of our analysis. This is necessary for all use
cases.

#### Function
The visualization component will take numerical and categorical data provided by the
analysis/projection component and generate maps, charts, and other graphics that will aid in the
understanding of the content.

#### Name
This component will reside in a Python module that will be named `visualization`.

#### Inputs
Each function within this component will take a data object produced by the projection component as
well as possibly some tunable options and parameters to be given through the user interface
component.

#### Outputs
This component will exclusively output data to be interpreted visually by the library chosen during
the technology review.

#### Operation
Operation of this component should be opaque to the majority of users.  Visualizations will be
generated dynamically within the user interface component by triggering callbacks when the user
changes options or interacts with the visualizations themselves.

----

### 5. User interface:
This will let the user interact with the data and get answers to their questions. It is necessary
for all use cases.

#### Function
The user interface component is the primary method that users will interact with the project.  It
will provide several graphical components that will provide both instruction and functionality.  The
initial plan is to build a dashboard-like interface with widgets consisting of:

 * Text for explanation/instruction
 * Sliders/dropdowns for selecting time periods
 * Buttons/Checkboxes for selecting fish species
 * Various displays from the mapping/visualization components

#### Name
This component will reside in a Python module that will be named `dashboard`.

#### Inputs
This component will take several inputs:

 * User input for interacting with widgets (using the chosen library for interface design)
 * Data from the future mapping/visualization component (including maps and charts)

#### Outputs
Operation of this component will result in the serving of a web server that will allow the user to
view and interact with the analysis in a web browser of their choosing.

#### Operation
Ultimately the goal of this component is to provide a single entry point to the project for outside
users.  We wish to have a product that for the purpose of the class presentation can be served on a
cloud provider but also has easy enough setup that it can be launched locally.

#### Further Details
The user interface will be formatted as a locally hosted web app with the following sub-components:
* create_static: generates the static components of the web app, including app header, broad overview description, and instructions for app use. Input: text to be displayed, either as a raw string or a separate text file (for longer descriptions). Output: Dash commands for generating the static components.
* create_map: generates an interactive map (base state) displaying the Columbia riverbed region with options to overlay color-coded icons representing salmon populations for different regions during a selected time period. Input: default salmon species (factor) and time (int) selections. Output: Dash commands for generating a graph component.
* update_species: updates the salmon map based on user-selected values for salmon species to display (checklist? Drop-down menu?). Input: user-selected values for salmon species (Factor with a value for each species). Output: Dash commands for generating an updated map graphic.
* update_time: updates the salmon map based on user-selected values for time-period to display (slider the user can drag, with time determined by slider position). Input: user-selected value for time (int). Output: Dash commands for generating an updated map graphic.
* launch_app.py: script to set up and locally launch the FutureFish app, with the default values for the interactive visualization component.
