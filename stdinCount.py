#!/usr/bin/python

#Line Count from Stdin Command

import sys
counter = 1
while True:
	line = sys.stdin.readline()
	if not line:
		break
	print "%s : %s" % (counter,line)
	counter = counter + 1

