This challenge by Capital One requires a deep analysis of the public data from the San Francisco Fire Department that contains dispatch 
information for emergency calls, with call time, location, and dispatch. Using this dataset, I have generated custom graphs to understand
key insights from the dataset. From investigating the dataset, these calls were made between 01/13/2018 - 01/24/2018.
## Optimizations & Analysis:
***Data Visuals: Display or graph 3 metrics or trends from the data set that are interesting to you.***
1. The first trend I found interesting in the data set was the units sent to certain calls in certain areas. In order to analyze this trend, I plotted sent unit types for calls in every region/location in San Fransisco. This revealed that two unit types,"Investigation" and "Support", had only specific regions that were called in the given region. These two plots are shown below:
![Investigation Regions](https://github.com/kmert10/Capital-One-SFPD-Challenge/blob/master/Website%20Graphs%20Images/cool%20thing%20part%201%20a.PNG/raw=true)
![Support Regions](https://github.com/kmert10/Capital-One-SFPD-Challenge/blob/master/Website%20Graphs%20Images/cool%20thing%20part%201%20b.PNG/raw=true)
This finding shows that these types of units can be located near these regions, which can improve responce time and effectiveness.
2. I've looked into different priorities and how often they change. To investigate this, I have created a heat map that looks at the differences between original priorities and final priorities.
![Change in Call Priority Heat Map](https://github.com/kmert10/Capital-One-SFPD-Challenge/blob/master/Website%20Graphs%20Images/Lower%20SF%20Original%20vs%20Final%20Prio%20Heat%20Map.PNG/raw=true)
The heat map above shows the change in call priority in lower San Fransisco. The spectrum towards the orange shows that the priority increased after receiving the call and the spectrum towards blue indicates the priority decreased after receiving calls. The gray-ish dots represents the calls that their priorities hasn't changed.  It is also important to know that I have converted numerical priorities as numbers that continue after 2 and 3. For *Lower SF*, the heat map is pretty constant which indicates that the priority assesment is done properly. However, it is important to note that there are more blue dots than orange dots which tells us that SFPD had casses where they under-asseses situations.
![Change in Call Priority Heat Map: Financial District](https://github.com/kmert10/Capital-One-SFPD-Challenge/blob/master/Website%20Graphs%20Images/Financial%20Dist%20Original%20vs%20Final%20Prio%20Heat%20Map.PNG/raw=true)
Looking at the heat map of the *Financial Disctrict's* heat map, it is pretty similar to *Lower SF's* heat map. 
