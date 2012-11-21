# -*- coding: utf-8 -*-

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
	# print rastr + ".00" + " " + decstr + ".0"
	return rastr + ".00" + " " + decstr + ".0"

def genMPCMag(mag):
	# TODO select color band
	if mag == 0:
		return "15.0 R"
	else:
		return str(round(mag,1)) + " R"

def genMPCNum(prefix,num):
	ret = prefix + str(int(num))
	if len(ret) > 12:
		return "NAME TOO LONG, error"
	ret = ret + (" " * (14-len(ret))) + "C"
	return ret

def genMPCObsy(obs):
	if len(obs) != 3:
		return " " * 6 + str(500)
	return " " * 6 + obs


"""
Base function of ths module. Generates a valid MPC string
which can be fet into the astchecker
"""
def genMPCString(prefix,number,utdate,ra,dec,mag,obscode):
	return genMPCNum(prefix,number) + genMPCDate(utdate) + " " + genMPCRADEC(ra,dec) + " "*10 + genMPCMag(mag) + genMPCObsy(obscode)

# genMPCString("RG",1323,'2012-02-01T20:15:11','10 18 24','+38 23 09',12.443,'C01')

