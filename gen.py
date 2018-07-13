import uuid
from datetime import datetime
import json
view = uuid.uuid1()

viewID = uuid.uuid1() 
item1 = "viewID:"
json1 = {"type": "Viewed", "data":{"viewID": str(uuid.uuid1()), "eventDateTime": str(datetime.now())}}
json.dumps(json1)
json2 = {"type": "Interacted", "data":{"viewID": json1['data']['viewID'], "eventDateTime": str(datetime.now())}}
json.dumps(json2)
print(json1)
print(json2)