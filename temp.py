
import requests
import argparse

parser = argparse.ArgumentParser()
#parser.add_argument("latitude",type = float)
#parser.add_argument("longitude",type = float)
parser.add_argument("tm", type =int)
args= parser.parse_args()

#from sys import argv
response = requests.get("https://api.darksky.net/forecast/b11ad4995e5003463aa7f750d36f0cb2/42.3601,-71.0589,args.tm?exclude=currently,flags")
print(response.status_code)
print(response.json())
print(args.tm)
with open ('mydata.json' ,'w') as f:
    json.dump(data,f)
