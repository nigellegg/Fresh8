import threading


class Generate():

    def __init__(self):
        self.data = []
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
        print(self.data)
        out = open(self.output+'data.txt', 'w')
        out.write(self.data)

        
    def checknsave(self):
        print("Check size of data and save... ")
        jdata = self.data
        print(jdata)
        views = []
        interact = []
        click = []
        out = open('events'+str(datetime.now())+'.json', 'w')
        while len(views) < self.batch:
            for x in jdata:
                if x['type'] == 'Viewed':
                    views.append(x['data']['viewID'])
                if x['type'] == 'Interacted':
                    interact.append(x['data']['viewID'])
                if x['type'] == 'Click Through':
                    click.append(x['data']['viewID'])
        for y in jdata:
            if y['data']['viewID'] in views:
                out.write(str(y))
        out.close()
            

    def run(self):
    	t1 = threading.Thread(target=self.create_data)
    	t2 = threading.Thread(target=self.checknsave)
    	t1.start()
    	t2.start()


if __name__ == '__main__':
	g = Generate()
	g.run()