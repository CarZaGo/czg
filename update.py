#!/bin/env python2
#code owner = "sachin"
#
import urllib2
import os

ver = open("version.txt", "r")
version = ver.read()
ver.close()

up = urllib2.urlopen("https://raw.githubusercontent.com/CarZaGo/czg/master/version.txt").read()
if version != up:
	print ""
	print "[+] Update available"
	print ""
	x = raw_input("Want to update y/n: ")
	if x == "y":
		os.remove("jdash.py")
		sachin = "https://raw.githubusercontent.com/CarZaGo/czg/master/czg.py"
		update = urllib2.urlopen(sachin).read()
		
		jdash = open("jdash.py", "w")
		jdash.write(update)
		jdash.close()

		os.remove("version.txt")
		ver = open("version.txt", "w")
		ver.write(up)
else:
	print ""
	print "[-] No update available right now"
	print ""
