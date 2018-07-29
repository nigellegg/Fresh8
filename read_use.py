import threading
import json
from datetime import datetime

class ReadUse():

    def __init__(self):
    	self.interval = int(sys.argv[1])
    	self.views = 0
    	self.interact = 0
    	self.click = 0
    	self.interclick = 0

    def read(self):
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
        t1.start()
        interval = self.interval
    	while True:
    	    t2.start()
            time.sleep(interval - ((time.time() - starttime) % interval))


if __name__ == '__main__':
	ru = ReadUse()
	ru.read()
	ru.use()