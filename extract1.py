import requests, sys, os, json, time

key = "b11ad4995e5003463aa7f750d36f0cb2"
latitude = "42.3601"
longitude = "-71.0589"
time = int(time.time())
time = str(time)

def takeInputs():
	try:
		latitude = str(sys.argv[1])
		longitude = str(sys.argv[2])
		tFlag = sys.argv[3]
		if tFlag == "-t":
			time = str(sys.argv[4])
	except:
		print("E R R O R !! arguments were missing")
		sys.exit(1)

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

#takeInputs()

api = "https://api.darksky.net/forecast/"+key+"/"+latitude+","+longitude+","+time+"?exclude=currently,daily,flags"
response = requests.get(api).json()
with open ('newData.json' ,'w') as f:
    json.dump(response,f, indent=3, sort_keys=False)

#loaded = loadJson("newData.json")

print(type(response))
for i in range(0,len(response["minutely"]["data"])):
	print(response["minutely"]["data"][i]["time"])
	print(response["minutely"]["data"][i]["precipIntensity"])
	print(response["minutely"]["data"][i]["precipProbability"])
	print("---------------------------\n")
