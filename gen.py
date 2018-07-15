import sys
import uuid
from datetime import datetime
import json
#view = uuid.uuid1()
import time

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
        interval = int(sys.argv[3])
        self.output = sys.argv[4]
        starttime=time.time()
        while True:
            self.checknsave()
            time.sleep(interval - ((time.time() - starttime) % interval))
	
    def create_data(self):
        groups = self.groups
        print('Need to create '+str(groups)+' groups.')
        i = 0
        while i<groups:
            json1 = {"type": "Viewed", "data":{"viewID": str(uuid.uuid1()), "eventDateTime": str(datetime.now())}}
            self.data = self.data+json1+'\n'
            if i % 20 == 0:
                json2 = {"type": "Interacted", "data":{"viewID": json1['data']['viewID'], "eventDateTime": str(datetime.now())}}
                self.data = self.data+json2+'\n'
            if i % 20 == 1: 
                json3 = {"type": "Click Through", "data":{"viewID": json1['data']['viewID'], "eventDateTime": str(datetime.now())}}
                self.data = self.data+json3+'\n'
            if i % 20 == 2:
                json4 = {"type":  "Interacted", "data":{"viewID": json1['data']['viewID'], "eventDateTime": str(datetime.now())}}
                json5 = {"type": "Click Through", "data":{"viewID": json1['data']['viewID'], "eventDateTime": str(datetime.now())}}
                self.data = self.data+json4+'\n'
                self.data = self.data+json5+'\n'
            i += 1

    def checknsave(self):
        print("Check size of data and save... ")




if __name__ == "__main__":
	gen_data = Generate()
	gen_data.create_data()