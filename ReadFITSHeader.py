# -*- coding: utf-8 -*-
import pyfits

def getRA(hdu):
	return str(hdu[0].header['OBJCTRA'])

def getDEC(hdu):
	return str(hdu[0].header['OBJCTDEC'])

def getUT(hdu):
	return str(hdu[0].header['DATE-OBS'])
