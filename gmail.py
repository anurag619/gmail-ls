#!/usr/bin/env python
"""download unread emails"""

import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup

def main():
	import getpass
	user = raw_input('gmail Username: ')
	passwd = getpass.getpass('gmail Password: ')
	r = requests.get('https://mail.google.com/mail/feed/atom', auth=HTTPBasicAuth(user, passwd))
	xml = r.text
	soup = BeautifulSoup(xml)
	print "the email with their subjects are:/n /n" 
	for sub in  soup.find_all('title'): 
	 print sub.text
	if (sub.text)=="Unauthorized":
	 print "wrong user-id or password, Please run the script again."
 
if __name__=='__main__':
 main()
