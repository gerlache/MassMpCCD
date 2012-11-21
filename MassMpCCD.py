#!/usr/bin/python
# -*- coding: utf-8 -*-

import BuildMPCLine
import ReadFITSHeader
import ReadConfig
import AstcheckParse
import pyfits
import os
import argparse
import ConfigParser
import glob
from subprocess import *

"""
Main program
"""

# simple comand line arg parser
parser = argparse.ArgumentParser(description="MassMpCCD - A Helper\
		Tool for MpCCD")
parser.add_argument('--fitdir', metavar='fitdir', help='directory\
		which hold the fits files')
parser.add_argument('--cfg', metavar='configf', help='configuration\
		file for MassMpCCD')
args = parser.parse_args()

# check if we have all cmd params
if args.cfg is None:
	parser.error('No config file specified')
if args.fitdir is None:
	parser.error('No FITS dir specified')

cfg = ReadConfig.openCfg(args.cfg)


# for each fits file in the fitsdir do
# generate mpc line
i = 1
for fitfile in glob.glob(args.fitdir+"/*.fit"):
	mpcstr = ""
	print "Reading " + fitfile
	hdulist = pyfits.open(fitfile)
	
	# read fits files and generate mpc string files
	try:
		mpcstr = BuildMPCLine.genMPCString("RG",i,
				ReadFITSHeader.getUT(hdulist),
				ReadFITSHeader.getRA(hdulist),
				ReadFITSHeader.getDEC(hdulist),15.0,'C01')
	except KeyError:
		print "This File misses at least one of the keys: \
			OBJCTRA, OBJCTDEC, DATE-OBS"
		hdulist.close()
		print ""
		break

	if len(mpcstr) != 80:
		hdulist.close()
		break

	try:
		f = open(fitfile+".fakempc",'w')
		f.write(mpcstr)
		f.close()
	except BaseException:
		print "Could not write MPC-String file"
		hdulist.close()
		print ""
		break

	hdulist.close()
	i = i + 1
	print ""

# now apply astcheck on each fake mpc file in the fits dir
for mpcfile in glob.glob(args.fitdir+"/*.fit.fakempc"):
	print "Searching for  " + mpcfile
	srad = cfg.get('massmpccd', 'searchrad')
	astout = Popen(["./astcheck",mpcfile,"-r"+str(srad)],
			stdout=PIPE).communicate()[0]
	try:
		# we write tis files only for later debugging purposes
		f = open(mpcfile+".astcheck","w")
		f.write(astout)
		f.close()
	except IOError:
		sys.exit()
	print AstcheckParse.parse(astout) 
	print ""
