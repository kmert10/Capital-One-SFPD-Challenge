This challenge by Capital One requires a deep analysis of the public data from the San Francisco Fire Department that contains dispatch 
<<<<<<< HEAD
information for emergency calls, with call time, location, and dispatch. Using this dataset, I have generated custom graphs to understand 
key insights from the dataset. 
## Opmizations & Analysis:
=======
information for emergency calls, with call time, location, and dispatch. Using this dataset, I have generated custom graphs to understand
key insights from the dataset. From investigating the dataset, these calls were made between 01/13/2018 - 01/24/2018.
## Optimizations & Analysis:
***Data Visuals: Display or graph 3 metrics or trends from the data set that are interesting to you.***
1. The first trend I found interesting in the data set was the units sent to certain calls in certain areas. In order to analyze this trend, I plotted sent unit types for calls in every region/location in San Fransisco. This revealed that two unit types,"Investigation" and "Support", had only specific regions that were called in the given region. These two plots are shown below:
![Investigation Regions](https://github.com/kmert10/Capital-One-SFPD-Challenge/blob/master/Website%20Graphs%20Images/cool%20thing%20part%201%20a.PNG?raw=true)
![Support Regions](https://github.com/kmert10/Capital-One-SFPD-Challenge/blob/master/Website%20Graphs%20Images/cool%20thing%20part%201%20b.PNG?raw=true)
This finding shows that these types of units can be located near these regions, which can improve responce time and effectiveness.
2. I've looked into different priorities and how often they change. To investigate this, I have created a heat map that looks at the differences between original priorities and final priorities.
![Change in Call Priority Heat Map](https://github.com/kmert10/Capital-One-SFPD-Challenge/blob/master/Website%20Graphs%20Images/Lower%20SF%20Original%20vs%20Final%20Prio%20Heat%20Map.PNG?raw=true)
The heat map above shows the change in call priority in lower San Fransisco. The spectrum towards the orange shows that the priority increased after receiving the call and the spectrum towards blue indicates the priority decreased after receiving calls. The gray-ish dots represents the calls that their priorities hasn't changed.  It is also important to know that I have converted numerical priorities as numbers that continue after 2 and 3. For *Lower SF*, the heat map is pretty constant which indicates that the priority assesment is done properly. However, it is important to note that there are more blue dots than orange dots which tells us that SFPD had casses where they under-asseses situations.
![Change in Call Priority Heat Map: Financial District](https://github.com/kmert10/Capital-One-SFPD-Challenge/blob/master/Website%20Graphs%20Images/Financial%20Dist%20Original%20vs%20Final%20Prio%20Heat%20Map.PNG?raw=true)
Looking at the heat map of the *Financial Disctrict's* heat map, it is pretty similar to *Lower SF's* heat map. The number of gray-ish calls is substantially larrger compared to colored calls. A key difference between the two heat maps, considering colored calls ,there are more orange calls compared to blue calls. This tells us that in the *Financial District*, the SFPD over-asses calls. This difference in two areas is a sign of the SFPD being more protective and careful in more populated regions of San Fransisco.
3. Considering the available unit types, the most common units dispatched are: Medics, Engine and Chief. A neat heat map that shows this is given below.
![Priority vs Unit Type Heat Map: Financial District](https://github.com/kmert10/Capital-One-SFPD-Challenge/blob/master/Website%20Graphs%20Images/Downtown%20Unit%20Type%20vs%20Original%20Prio%20Heat%20Map.PNG?raw=true)
The majority of the dots are from these three unit types and it clear that these units are assigned higher original priorities. This claim can be relatable beacuse in an emergency that might be life threataning, these three units are the ones that basically will save lives or many people.

***Given an address and time, what is the most likely dispatch to be required?***
In order to address this question, first, I created a scatter plot to see what might be correlated.
![Scatter Zip Unit Hour](https://github.com/kmert10/Capital-One-SFPD-Challenge/blob/master/Website%20Graphs%20Images/Scatter%20plot%20of%20zipcodes%20vs%20hours%20of%20units.png?raw=true)
This scatter plot of a portion of the given dataset, which we can use as a tool to understand the correlation. The y-axis of the plot represents the two least-significant digits of the zip codes, the x-axis represents the time in hours a and the color represents the unit types, which is shown in the legend. Although this scatter plot shows just a random portion of the dataset, it is important to notice the ratio of each unit. The first thing we notice is that the plot is green and pink dominant, which means that in each hour of the day, there is a need for a "Truck" and a "Medic". A need for an "Engine" starts early in the morning while a need for the "Chief" and the "Private" starts in the noon. If we look at the figure: 
![San Fransisco Zip Code Map](http://www.healthysf.org/bdi/outcomes/images/zip-map.jpg?raw=true) 

we can us this map to decode the y-axis of the plot and cross reference the addresses of required units. 


***Which areas take the longest time to dispatch to on average? How can this be reduced?***
>>>>>>> master
