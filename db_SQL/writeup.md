SQL while popular, is best as a data store for certain types of data. 

In this exercise, I had attempted to store our airport.json data into a database with a table for airport name and code and a table
for the data associated with the code. 

### Challenges:

SQL was not built to store data from a json file. One has to convert the json to a db/csv file or another that could be easily placed
into the database. In the json format, data is stored more of as clusters rather than relationally and especially in our airports.json
file, this was the case. Therefore when inserting the data into the SQL db, it was a more convoluted task than expected. An incorrect way
would have been to directly import all data into one column. The preferred way is to see what is related in the data, in my case, I 
clustered a name/code and the data associated. 

### SQL vs MongoDB:

MongoDB is simply easier to get started with than SQL. With MongoDB, a json file can be easily added to the database and already clustered.
It is abstract such that the data does not have to be well defined. With SQL, one has to first create tables, and then specify what data 
type and insert data following a specific schema. 

A SQL database is definitely easier to use when there is lots of data to be stored relationally, not from a given file. This is because 
one can insert each column of data per cluster of data received and not have to translate a given set of data into tables. 

### Conclusions:

One must clearly define what sort of data is being stored before choosing a database. 

For example, in the case of airports.json, MongoDB should be a preferred data storage format because it automatically clusters the data
to an ID, and it is simply easier to read a json file using MongoDB. In addition, programs with various abstract unrelated data may 
benefit from MongoDB.

In any relational data set, SQL will be a better fit. It provides structure to the data and a clear relational format.

e.g 

UserID -> webpage2 -> log1

UserID -> webpage1 -> form1
