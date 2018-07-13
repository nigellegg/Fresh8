import sys
import uuid
from datetime import datetime
import json
view = uuid.uuid1()

'''viewID = uuid.uuid1() 
item1 = "viewID:"

json.dumps(json1)
json2 = {"type": "Interacted", "data":{"viewID": json1['data']['viewID'], "eventDateTime": str(datetime.now())}}
json.dumps(json2)
print(json1)
print(json2)
'''

class Generate():

	def __init__(self):
	    self.data = '' 
	    self.groups = int(sys.argv[1])
	    self.batch = int(sys.argv[2])
	    self.interval = int(sys.argv[3])
	    self.output = sys.argv[4]
	
	def create_view(self):
		groups = self.groups
		print('Need to create '+str(groups)+' groups.')
        json1 = {"type": "Viewed", "data":{"viewID": str(uuid.uuid1()), "eventDateTime": str(datetime.now())}}



if __name__ == "__main__":
	gen_data = Generate()
	gen_data.create_view()