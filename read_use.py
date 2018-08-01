import threading
import json
from datetime import datetime
import time
import os

class ReadUse():

    def __init__(self):
        self.interval = int(sys.argv[1])
        self.views = 0
        self.interact = 0
        self.click = 0
        self.interclick = 0

    def read(self):
        files = os.listdir('./data')
        now = datetime.now()
        diff = []
        for f in files: 
            tstamp = f[6:]
            diff.append(now - tstamp)
        fuse = diff.index(min(diff))
        usef = files[fuse]
        text = open(usef)
        
        cviews = 0
        cinteract = 0
        cclick = 0
        interclick = 0 
        inter = 0
        
        for line in text:
            line = json.dumps(line)
            if line['type'] ==  'Viewed':
                cviews += 1
                vid = x['data']['viewID']
            if line['type'] == 'Interaction':
                cinteract += 1
                inter = 1
            if line['type'] == 'Click' and inter == 0:
                cclick += 1
            if line['type'] == 'Click' and inter == 1:
                cinterclick += 1 
        
        print('Views', str(cviews))
        print('Interact', str(cinteract))
        print('Click through', cclick)
        print('interact and click through', cinterclick)

        return True


    def run(self):
        t1 = threading.Thread(target=self.read)
        interval = self.interval
        while True:
            t1.start()
            time.sleep(interval - (int((datetime.now()-starttime).seconds) % interval))


if __name__ == '__main__':
    starttime = datetime.now()
    ru = ReadUse()
    ru.run()