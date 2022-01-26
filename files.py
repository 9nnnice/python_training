import json

f = open("c:/temp/py/config.json")
res = json.load(f)
f.close()

print(res)