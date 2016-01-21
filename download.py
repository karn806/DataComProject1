#!/usr/bin/env python
import socket as sk
from itertools import islice

def mkDownloadRequest(serv, objName):
	return ("GET {o} HTTP/1.1\r\n" + "Host: {s}"+"\r\n\r\n").format(o=objName, s=serv)

# print "{!r}".format(mkDownloadRequest("intranet.mahidol", "/"))

servName = 'intranet.mahidol'
port = 80
## create an empty socket
sock = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
## connect to a destination as specified by the pair
sock.connect((servName, port))

request = mkDownloadRequest(servName, "/")
sock.send(request)

while True:
	data = sock.recv(1024)
	# print data
	#print type(data)
	with open('keepData.txt','w') as f:
		f.write(data)
	with open('keepData.txt','r') as r:
		File = r.read()
	print File
	# file = open('keepData.txt', 'r')
	# print file.read()	
	# file = open("keepData.txt", "w")
	
	# print type(readFile)
	# CL = "Content-Length: "
	# if CL in keepData.txt:
	# 	findIndexofContentLength = readFile.find(CL)
	# 	print findIndexofContentLength


	# if len(data)==0:
	sock.close()
	break
