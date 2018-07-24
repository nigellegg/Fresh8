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

Operation:
Clone the project from https://github.com/nigellegg/fresh8 to a directory on your machine.  
Run from a command line, eg 
	python3 gendata.py 10000 500 1 './data/'
	
Threading is used to run the data creation and file save functions in parallel
within this single script.    



