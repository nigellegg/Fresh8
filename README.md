# Fresh8 Test.  

There are two modules to be built: 
1.  Data Generation and "streaming". 
2.  Data ingestion. 

There are two scripts, written and run in Python3.  
I attempted a first pass in Go, but it was taking far too long to work out.  That might
have been a better option for this task.  I also attempted to put this on Google Cloud, 
but had problems installing the SDK, so it is a totally offline app.   

1. Data Generation - gendata.py
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

2. Data ingestion - read_use.py
Collection and counting script
read_use.py: run using python3 read_use.py 5, where the argument, 5, is the time interval between checks.  



