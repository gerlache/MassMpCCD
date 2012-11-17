import pyfits

def getRA(hdu):
	return str(hdu[0].header['OBJCTRA'])

def getDEC(hdu):
	return str(hdu[0].header['OBJCTDEC'])

def getUT(hdu):
	return str(hdu[0].header['DATE-OBS'])

hdulist = pyfits.open('142401_L20c06000s001.fit')

print getRA(hdulist) 
print getDEC(hdulist)
print getUT(hdulist)

hdulist.close()
