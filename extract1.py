import requests, sys, os, json, re

def takeInputs():
	try:
		latitude = sys.argv[1]
		longitude = sys.argv[2]
	except:
		print("E R R O R !! arguments were missing")
		sys.exit(1)

latitude = "42.3601"
longitude = "-71.0589"
#takeInputs()
key = "b11ad4995e5003463aa7f750d36f0cb2"
time = ""

api = "https://api.darksky.net/forecast/+"key+"/"+latitude+","+longitude+","+time+"?exclude=currently,flags"
print(api)
#from sys import argv
response = requests.get(api)
print(response.status_code)
print(response.json())
print(args.tm)
with open ('mydata.json' ,'w') as f:
    json.dump(data,f)
