US Bikeshare analysis program for 3 cities Chicago, Washington & New York City, is a part of Udacity data analysis nano degree program.

program is written using python 3.9
 
User is prompted to enter a city name , select a month & select a date which are the filters for the program.

Below are the resources that helped in exploring and writing the program:

Pandas
1- dt.month : https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.month.html
2- dt.hour: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.hour.html
3- dt.day_name: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.day_name.html
4- read_csv: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
5- group_by: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.groupby.html
6- count: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.count.html
7- nlargest: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.nlargest.html
8- fillna: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.fillna.html
9- Find most common combination of start station and ending station :
https://stackoverflow.com/questions/50848454/pulling-most-frequent-combination-from-csv-columns



The Datasets
-------------
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

Start Time (e.g., 2017-01-01 00:07:57)
End Time (e.g., 2017-01-01 00:20:53)
Trip Duration (in seconds - e.g., 776)
Start Station (e.g., Broadway & Barry Ave)
End Station (e.g., Sedgwick St & North Ave)
User Type (Subscriber or Customer)
The Chicago and New York City files also have the following two columns:

Gender
Birth Year

Statistics Computed
-------------------
#1 Popular times of travel (i.e., occurs most often in the start time)

most common month
most common day of week
most common hour of day

#2 Popular stations and trip

most common start station
most common end station
most common trip from start to end (i.e., most frequent combination of start station and end station)

#3 Trip duration

total travel time
average travel time
#4 User info

counts of each user type
counts of each gender (only available for NYC and Chicago)
earliest, most recent, most common year of birth (only available for NYC and Chicago)

