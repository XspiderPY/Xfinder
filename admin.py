#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("adminlinks.txt","r");
	link = raw_input("Enter Site  \n(ex : example.com or www.example.com ): ")
	print "\n\nAvilable links : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "OK Admin is=====> ",req_link

def Credit():
	Space(9); print "#####################################"
	Space(9); print "#         +++ Xfinder v1 +++        #"
	Space(9); print "#            by X spider            #"
	Space(9); print "#     team of  Union of Hacker      #"
	Space(9); print "#####################################"

Credit()
findAdmin()
