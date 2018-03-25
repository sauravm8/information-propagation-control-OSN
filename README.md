# information-propagation-control-OSN
Code-Dump of Project. 

The code creates a dictionary of randomised values for number of users configurable via config file and number of weeks configurable via config
file and save it as a pickle file in data folder. There is no code to do qualitative analysis yet.

For example if there were 2 users for 3 weeks

{0:[r01, r02, r03], 1:[r11, r12, r13]}

A data structure like this will be generated and stored. The random range is configurable through the config file.

26-03-2018

Another code was written to load the initial values and create a list of lists of the mean of the values, sliced according to the
number of weeks required.

Then the values are stored again as another pickle file

Next we will have to plot the graph