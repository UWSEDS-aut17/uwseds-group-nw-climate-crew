# How to use FutureFish: 
----
## How to download and run FutureFish: 

1. In a terminal window, navigate the the location you would like to copy the FutureFish files.

2. Clone the git repository in that location by typing the following in a terminal window:
~~~~
git clone https://github.com/UWSEDS-aut17/uwseds-group-nw-climate-crew.git
~~~~

3. In the uwseds-group-nw-climate-crew directory, initiate the setup by typing:
~~~~
python setup.py develop --user
~~~~

4. Then, you can run the visualization from the uwseds-group-nw-climate-crew directory by typing the following in the terminal.
~~~~
python ./scripts/futurefish_dash.py
~~~~

5. Then copy the following url into your browser to navigate to the application. 
~~~~
http://127.0.0.1:5000/
~~~~

6. Enjoy exploring FutureFish! The homescreen of the FutureFish tool is shown below. 

<p align="center">
  <img src="https://github.com/UWSEDS-aut17/uwseds-group-nw-climate-crew/blob/master/futurefish/resources/images/home_screen.png">
</p>

----

## FutureFish features: 

1. __Sort by specie__: 
	Use the dropdown menu to specify which specie of salmon you are interested in. FutureFish contains data for Chinook, Sockeye, Coho, and Pink salmon.

<p align="center">
  <img src="https://github.com/UWSEDS-aut17/uwseds-group-nw-climate-crew/blob/master/futurefish/resources/images/dropdown.png">
</p>

2. __Select time period__: 
	The FutureFish tool is meant to help visualize where salmon may swim in the future. Choose a time period of interest with the buttons below the dropdown menu. 

<p align="center">
  <img src="https://github.com/UWSEDS-aut17/uwseds-group-nw-climate-crew/blob/master/futurefish/resources/images/time_period_button.png">
</p>

3. __Lock View feature__: 
	When comparing different species and time periods, you may want to use the _Lock View_ feature. When you select _Lock View_ at the bottom of the map, the area of the map in view will remain the same when you select other options (i.e. another specie or time period). Select _Refresh View_ to return to the default zoom and area shown. 

_Lock View_:
<p align="center">
  <img src="https://github.com/UWSEDS-aut17/uwseds-group-nw-climate-crew/blob/master/futurefish/resources/images/lock_view.png">
</p>

_Refresh View_:
<p align="center">
  <img src="https://github.com/UWSEDS-aut17/uwseds-group-nw-climate-crew/blob/master/futurefish/resources/images/refresh_view.png">
</p>
 
