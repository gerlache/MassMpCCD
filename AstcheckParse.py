# -*- coding: utf-8 -*-
import re

# ao = stdout of astcheck tool
# TODO just coded to work (somehow) ... can be done very much more elegant
def parse(ao):
	num = ""
	year = ""
	unum = ""
	mag = ""

	retlist = []
	for l in iter(ao.splitlines()):
		# look if numbered object
		num = l[0:8]
		if re.search('\(*\)', num):
			num = num.strip().replace('(','').replace(')','')
		else:
			num = ""

		# look if year is present
		year = l[9:14].strip()
		if not re.search('[0-9][0-9][0-9][0-9]',year):
			year = ""

		# look if preliminary number is present
		unum = l[14:21].strip()
		if not re.search('[A-Z][0-9]',unum):
			unum = ""
		# get magnitude
		mag = l[51:56].strip()
		if not re.search('[0-9]\.[0-9]',mag):
			mag = ""

		if unum != "" :
#			print "debg "  + num + unum + year + mag
			retlist.append((num,year,unum,mag))
	return retlist

