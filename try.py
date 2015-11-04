#!/usr/bin/python

import sys
try:
	s = raw_input('Enter something----->')
except EOFError:
	print "\nwhy did you do an EOF on me?"
	sys.exit()
except:
	print "\nsome error/exception occured."
print "done"
