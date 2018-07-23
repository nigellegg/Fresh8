# Fresh8 Test.  

There are two modules to be built: 
1.  Data Generation and "streaming". 
2.  Data ingestion. 

Data Generation - gendata.py
called using python gen.py with the following command line arguments:
	- number of groups (integer) - number of event groups created
	- batch-size (integer) - number of event groups per output file
	- interval (integer) - interval in seconds between each file creation.
	- output directory (string) - where files are saved to. 

Threading is used to run the data creation and file save functions in parallel
within this single script.    



