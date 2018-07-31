import threading    
import sys
import json
import time
from datetime import datetime
import uuid


class Generate():

    def __init__(self):
        self.data = []
        self.groups = int(sys.argv[1])
        self.batch = int(sys.argv[2])
        self.interval = int(sys.argv[3])
        self.output = sys.argv[4]
        starttime=time.time()
        

    def create_data(self):
        '''
        Generates the JSON data. 
        Data is written to the class variable, self.data.  
        Volume of data created is taken from the class variable, self.groups
        '''

        groups = self.groups
        print('Need to create '+str(groups)+' groups.')
        
        i = 0
        while i<groups:
            json1 = {"type": "Viewed", "data":{"viewID": str(uuid.uuid1()), "eventDateTime": str(datetime.now())}}
            self.data.append(json1)
            if i % 20 == 0:
                json2 = {"type": "Interacted", "data":{"viewID": json1['data']['viewID'], "eventDateTime": str(datetime.now())}}
                self.data.append(json2) 
            if i % 2 == 1: 
                json3 = {"type": "Click Through", "data":{"viewID": json1['data']['viewID'], "eventDateTime": str(datetime.now())}}
                self.data.append(json3)
            if i % 20 == 2:
                json4 = {"type":  "Interacted", "data":{"viewID": json1['data']['viewID'], "eventDateTime": str(datetime.now())}}
                json5 = {"type": "Click Through", "data":{"viewID": json1['data']['viewID'], "eventDateTime": str(datetime.now())}}
                self.data.append(json4)
                self.data.append(json5)
            i += 1
        
        
    def checknsave(self):
        '''
        Run on a timer.  
        Takes the class variable, self.data, and writes out the correct number of groups
        to the output file. 
        '''

        print("Check size of data and save... ")
        jdata = self.data
        views = []
        interact = []
        click = []
        out = open('events'+str(datetime.now())+'.json', 'w')
        while len(views) < self.batch:
            for x in jdata:
                print(x)
                #x = json.loads(x)
                if x['type'] == 'Viewed':
                    views.append(x['data']['viewID'])
                if x['type'] == 'Interacted':
                    interact.append(x['data']['viewID'])
                if x['type'] == 'Click Through':
                    click.append(x['data']['viewID'])
        for y in jdata:
            if y['data']['viewID'] in views:
                json.dump(y, out)
        out.close()
            

    def run(self):
        t1 = threading.Thread(target=self.create_data)
        t2 = threading.Thread(target=self.checknsave)
        t1.start()
        interval = self.interval
        while True:
            t2.start()
            time.sleep(interval - (int((datetime.now()-starttime).seconds) % interval))


if __name__ == '__main__':
    starttime = datetime.now()
    g = Generate()
    g.run()