#!/usr/bin/python

import hashlib
import time
import base64
import re
import urllib2
import sys
import os
from datetime import datetime  
from datetime import timedelta 
import time
import getopt
import requests
import json
import msvcrt



COMMANDS = ['to do']
#PROD settings
UNLOCKD_PROD = 'https://rewards.prod.eu.unlockd.com/v1/eligible-users/'

#Sandbox settings
UNLOCKD_SANDBOX = 'https://rewards.preview.mq.unlockd.com/v1/eligible-users/'



def make_url(path, query_params = None):
	url = ROOT_URL + path	
	if query_params != None and query_params != '':
		url = url  + '?' + query_params
	return url



def main(argv):

	try:
	  opts, args = getopt.getopt(argv,"a:p")
	except getopt.GetoptError, error:
	  print_options_manual()
	  sys.exit(2)

	api_key = ''
	use_prod = False

	for opt, arg in opts:
	  if opt == '-h':
	     print_options_manual()
	     sys.exit()
	  elif opt == "-a":
	     api_key = arg
	  elif opt == "-p":
	     use_prod = True
	  

	if api_key == '':
		print_options_manual()
		sys.exit(2)
	

	
	

	if use_prod == True: #use PROD
		#print 'are you sure you want to run commands on Unlockd PROD? Press Y to continue'
		#c = msvcrt.getch()
		#if c == 'y' or c == 'Y':
			eligibility_url = UNLOCKD_PROD			
		#else:
		#	sys.exit(2)
	else:
		#DEV
		eligibility_url = UNLOCKD_SANDBOX	




	
	
	
	#GET PlaylistFeedTasteProfiles	
	executeCommand(api_key, 'get', eligibility_url)

	
	return



	


def print_options_manual():
	print 'unlockd_tester.py'
	print '      E.g. unlockd_tester.py -a 123456'

def generateOAuthToken(key_file):

	#salt value is written in my MQ Useful Info

	scopes = ['https://www.googleapis.com/auth/userinfo.email']

	print 'generating oauth token'
	credentials = ServiceAccountCredentials.from_json_keyfile_name(key_file, scopes)
	#http = credentials.authorize(httplib2.Http())
	print credentials.get_access_token().access_token
	return credentials.get_access_token().access_token


def executeCommand(api_key, method, url, customParamKey = None):

	


	headers = {"AUTH-APIKEY" : api_key}
	urlparams = {}
	if customParamKey != None:
		urlparams[customParamKey] = customParamVal
	
 	r = requests.get(url, headers = headers, params = urlparams)
 	print r.url
 	print r.status_code
 	try:
		js = r.json()
		print js.dumps(js,indent = 2, sort_keys=True, separators=(',', ': ')).encode('utf8')
 	except Exception, error:
 		print r.text.encode('utf8')

if __name__ == "__main__":
   main(sys.argv[1:])