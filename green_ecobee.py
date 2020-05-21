#!/usr/bin/env python3
import sys, os
import datetime
import requests
import csv

headers = {
# UPDATE AUTH STRING
	'Authorization': 'Basic YWRtaW46YWRtaW4='}
weekno = datetime.datetime.today().weekday()

# UPDATE IFTTT MAKER WEBHOOK KEY
key = 'sample_key'
# source from hardcoded list
#known_macs = ('AA:AA','ZZ:ZZ')
# source from file
with open('known_macs', 'r') as f:
	raw_mac_list = f.readlines()
known_macs = [x[:-1] for x in raw_mac_list]
known_macs = [x[-5:] for x in known_macs]

# location for DD-WRT,  IP & url might use https depending on firmware settings
response = requests.get('http://10.0.0.1/Status_Wireless.live.asp', headers=headers)
content = str(response.content)
current_datetime = str(datetime.datetime.now().strftime("%Y-%m-%dT%H:%M"))

if response.status_code != 200:
	invalid_response = [current_datetime,'NA',response.status_code]
	with open(r'ecobee_setting.csv','a') as log:
		writer = csv.writer(log)
		writer.writerow(invalid_response)

# sends webhook "someone_home" if any mac present, or "both_away" if none present
# additional setting of "home_weekend" if any mac present on Saturday or Sunday
if any(s in content for s in known_macs) and response.status_code == 200:
	if weekno<5:
		home_req = requests.get('https://maker.ifttt.com/trigger/someone_home/with/key/' + key)
		home_response = [current_datetime,'someone_home',str(home_req.status_code)]
		with open(r'ecobee_setting.csv','a') as log:
			writer = csv.writer(log)
			writer.writerow(home_response)
	else:
		away_req = requests.get('https://maker.ifttt.com/trigger/home_weekend/with/key/' + key)
		with open(r'ecobee_setting.csv','a') as log:
			writer = csv.writer(log)
			writer.writerow(home_response)

if not any(s in content for s in known_macs) and response.status_code == 200:
	away_req = requests.get('https://maker.ifttt.com/trigger/both_away/with/key/' + key)
	away_response = [current_datetime,'away',str(home_req.status_code)]
	with open(r'ecobee_setting.csv','a') as log:
		writer = csv.writer(log)
		writer.writerow(away_response)
