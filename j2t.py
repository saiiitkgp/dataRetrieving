import os, json
from json2table import convert

def loadJson(jsonName):
	try:
		if os.path.isfile(jsonName):
			with open(jsonName) as js:
				dit=json.load(js)
			return dit
		else:
			print("E R R O R !! "+jsonName+" file is not present in the directory")
	except Exception as e:
			print(e)

json_object = loadJson("fullData.json")

build_direction = "LEFT_TO_RIGHT"
table_attributes = {"style" : "width:100%"}
html = convert(json_object, build_direction=build_direction, table_attributes=table_attributes)
print(html)