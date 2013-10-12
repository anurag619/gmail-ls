#!/usr/bin/env python

"""download unread emails"""

import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup

def main():
	import getpass
	user = raw_input('gmail Username: ')
	passwd = getpass.getpass('gmail Password:')
        print "reading the latest mail titles, please be a little patient..."
	url = 'https://mail.google.com/mail/feed/atom'
	r = requests.get(url, auth=HTTPBasicAuth(user, passwd) )
	xml = r.text
	soup = BeautifulSoup(xml) 
	for sub in  soup.find_all('title'): 
		print "\n" + sub.text +"\n"
	if (sub.text)=="Unauthorized":
		print "wrong user-id or password, Please run the script again.\n"
	

if __name__=='__main__':
	main()


