#! /usr/bin/env python

#Copyright HT srl, 2009-2010
#http://www.hackingteam.it/ for more information

#cod

"""
url encoders
Concatenate a string in form http://host:port/file
"""

VERSION = "1.0"

NAME="url_encoder"
DESCRIPTION="url_encoder"
DOCUMENTATION={}
DOCUMENTATION["VENDOR"] = "HT srl"
DOCUMENTATION["Repeatability"] = "not applicable"
DOCUMENTATION["Author"] = "cod"
DOCUMENTATION["Notes"] = ""

import os
import sys
from random import *
import struct

class url_encoder:

	r = None
	
	"""
	initialize object (shellcode and Random object)
	"""
	def __init__(self):
		self.r = Random()
	
	"""
	return a random char from a range
	"""
	def getrandchar(self):
		chars = "q0w1e2r3t4y5u6i7o8p9a_sdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
		i = self.r.randint(0, len(chars)-1)
		return chars[i]

	"""
	return a file name (random dot exe)
	"""
	def randfilename(self):
		newfilename = ""
		
		for i in range(8):
			newfilename += struct.pack('c', self.getrandchar())
		
		newfilename += struct.pack('cccc', '.', 'e', 'x', 'e')
		
		return newfilename

	def get(self, url, filename):
		
		value = url
		
		if (url.endswith("/") == False):
			value += "/"
		
		index = filename.rfind("/")
		
		if (index == -1):
			index = filename.rfind("\\")

		if  (index != -1):
			filename = filename[index+1:]

		value += filename
		
		return value
		
if __name__ == "__main__":
	print "url/encoder"
	
	myclass = url_encoder()
	
	print myclass.get(sys.argv[1], sys.argv[2])
	
