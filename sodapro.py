import requests, sys, os, json, time
import webbrowser



def takeInputs():
	try:

		latitude= str(sys.argv[1])
		longitude = str(sys.argv[2])
        altitude=str(sys.argv[3])
        date_begin= str(sys.argv[4])
        date_end=str(sys.argv[5])

	except:
		print("E R R O R !! arguments were missing")
		sys.exit(1)

takeInputs()

url = "http://www.soda-is.com/service/wps?Service=WPS&Request=Execute&Identifier=get_mcclear&version=1.0.0&DataInputs=latitude="+latitude+";longitude="+longitude+";
 altitude="+altitude+";date_begin="+date_begin+";date_end="+date_end+";time_ref=UT;summarization=PT15M;username=sahukara.krishna_sai%2540siemens.com&RawDataOutput=irradiation"

webbrowser.open(url)
