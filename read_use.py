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
        interact = 0
        click = 0
        interclick = 0 
        for line in text:
            line = json.dumps(line)
            if line['type'] ==  'Viewed':
                cviews += 1
        self.views = cviews
    	self.interact = cinteract
    	self.click = cclick
    	self.interclick = cinterclick
    	return True

    def use(self):
    	views = self.views
    	interact = self.interact
    	click = self.click
    	interclick = self.interclick
    	return True


    def run(self):
    	t1 = threading.Thread(target=self.read)
    	t2 = threading.Thread(target=self.use)
        interval = self.interval
        while True:
            t1.start()
            time.sleep(interval - ((time.time() - starttime) % interval))
    	while True:
    	    t2.start()
            time.sleep(interval - ((time.time() - starttime) % interval))


if __name__ == '__main__':
	starttime = datetime.now()
	ru = ReadUse()
	ru.read()
	ru.use()