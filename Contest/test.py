import json
import time
start = time.time()
f = open('./static/json/questionsTagDiffi.json')
data = json.load(f)
f.close()
print(time.time() - start)