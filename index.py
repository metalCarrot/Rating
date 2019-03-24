import json
from pprint import pprint

with open('rating.json') as f:
    data = json.load(f)

for key in data:
	marks = list(key.get('subjects').values())
	pprint((int(marks[0]) + int(marks[1]) + int(marks[2])) // 3)