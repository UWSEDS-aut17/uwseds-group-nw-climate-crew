<p align="center">
  <img src="https://github.com/UWSEDS-aut17/uwseds-group-nw-climate-crew/blob/master/futurefish/resources/images/logo_3.png">
</p>

## The Problem:
Climate change will have large effects on water resources all over the world. For this project we want to investigate how these changes will affect salmon in the Pacific Northwest. This question is often complicated by the fact that the Columbia River is highly regulated with dams which can have detrimental impacts on fish habitat. We will envision a world without any human infrastructure impacts to pose the question: __What impact will climate change _alone_ have on the viable of salmon habitat in the Pacific Northwest?__

To answer this question we worked with two datasets which project stream conditions well into the 21st century along with a simple model to estimate salmon viability. The two datasets we used are:
1. [Projections of streamflow](http://hydro.washington.edu/CRCC/) within the Columbia River Basin
2. [Temperature projections](https://www.fs.fed.us/rm/boise/AWAE/projects/NorWeST.html) for the same area.

# What is FutureFish?
FutureFish is a visualization tool that shows how viable salmon life is at hundreds of points around the Pacific Northwest both now and in the future. The data is categorized by salmon specie and a viability metric (see further explanation below). Users can choose a specie of salmon and time period of interest and explore where warming stream temperatures and diminishing snowpack will have the largest affect on salmon.  

<p align="center">
  <img src="https://github.com/UWSEDS-aut17/uwseds-group-nw-climate-crew/blob/master/futurefish/resources/images/futurefish_map.png">
</p>

### How can FutureFish be used?
We anticipate this visualization tool being useful for the following applications:
1. __Educational__:  
    This tool can be used in a classroom setting and provide an interactive way for students to engage with where salmon live now and where they might live in the future.
2. __Recreational__:  
    Recreational users can examine this interacive map to see how their fishing spots may change in the future.
3. __Environmental__:  
    Environmental groups can use this tool to show the impacts of climate change on salmon in a visual and interactive way.


### How to run FutureFish:
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

6. Enjoy exploring FutureFish!

### How we got our results:
We used three datasets to get our results:
1. Streamflow:  
    Streamflow data accessed from the [Columbia River Climate Change Project](http://hydro.washington.edu/CRCC/).
2. Stream temperature:  
    Stream temperature accessed from [NorWeST Stream Temperature Dataset](https://www.fs.fed.us/rm/boise/AWAE/projects/NorWeST.html#downloads) provided by the Rocky Mountain Research Station.
3. Biological models:  
    Two biological models were combined to capture the salmon population performance in response to  changes in streamflow (Snyder, 1996) and stream temperature (Swift, 1979).

Final model outputs were translated into fish vulnerability ranks of 1-5. 1 shows that fish populations are under most threat and 5 shows that the population is in good health. 

![alt text](http://hydro.washington.edu/CRCC/assets/img/CRBaerial.jpg)
