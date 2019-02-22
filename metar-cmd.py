#!/usr/bin/python3

import urllib3
import xml.etree.ElementTree as ET
import sys
import xmltodict
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def main():
	while(True):
		stations = []
		metars = []
		if (sys.argv[1] == "-t"):
			first_arg = 2
		else:
			first_arg = 1

		for x in sys.argv[first_arg:]:
			if (len(x) != 4):
				print("Error! Invalid command line argument!")
				return -1
			x = x.upper()
			stations.append(x)
		num = len(stations)
		url = "https://www.aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&hoursBeforeNow=3&stationString="
		i = 0
		while (i <= num - 1):
			url = url + stations[i]
			if (i != num - 1):
				url = url + ","
			i += 1

		http = urllib3.PoolManager()
		response = http.request('GET', url)
		xml_dict = xmltodict.parse(response.data)

		print("\n\n---------------------------------------------------------------------------------------")

		j = 0
		while (j < num):

			print(xml_dict['response']['data']['METAR'][j]['raw_text'])
			print("---------------------------------------------------------------------------------------")
			j += 1

		print("\n")

		# If -t is not passed as an argument, the update timer will be displayed.
		# If -t IS passed, the timer won't be displayed
		if (first_arg == 1):
			t = 300
			while (t):
				mins, secs = divmod(t, 60)
        			timeformat = '{:02d}:{:02d}'.format(mins, secs)
        			sys.stdout.write("Updating in: " + timeformat + "\r")
				sys.stdout.flush()
        			time.sleep(1)
        			t -= 1

			sys.stdout.write("                       \r")
			sys.stdout.flush()
		else:
			time.sleep(300)





if __name__ == "__main__":
    main()
