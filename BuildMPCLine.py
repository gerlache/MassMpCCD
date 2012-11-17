def genMPCDate(fdatestr):
	# 2012-02-01T20:15:11
	# RG111         C2012 08 01.90956 17 27 17.21 +75 26 11.2          17.1 R      C01
	
	# TODO parse date via regex, which can be configured
	y = fdatestr[0:4]
	mo = fdatestr[5:7]
	d = fdatestr[8:10]
	h = fdatestr[11:13]
	mi = fdatestr[14:16]
	s = fdatestr[17:]
	dayfrac = (float(h)*3600.0 + float(mi)*60.0 + float(s))/(3600.0*24.0)
	
	# TODO rounding cutoff, can be make better
	# print y + " " + mo + " " + d + "." + str(dayfrac)[2:7]
	return y + " " + mo + " " + d + "." + str(dayfrac)[2:7]

def genMPCRADEC(rastr,decstr):
	# TODO are there other sizes of the strings?
	print rastr + ".00" + " " + decstr + ".0"
	return rastr + ".00" + " " + decstr + ".0"

genMPCDate('2012-02-01T20:15:11')
genMPCRADEC('10 18 24','+38 23 09')
