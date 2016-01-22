#!/usr/bin/env python
import socket as sk

def mkDownloadRequest(serv, objName):
	return ("GET {o} HTTP/1.1\r\n" + "Host: {s}"+"\r\n\r\n").format(o=objName, s=serv)

#print "{!r}".format(mkDownloadRequest("intranet.mahidol", "/"))

servName = "www.google.com"
port = 80
## create an empty socket
sock = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
## connect to a destination as specified by the pair
sock.connect((servName, port))

request = mkDownloadRequest(servName, "/")
sock.send(request)

while True:
	data = sock.recv(1024)
	print data
	# if "\r\n\r\n" in data:
	# 	index = data.find("Content-Length: ")
	# 	# print index
	# 	ContentLength = data[index:]
	# 	#print ContentLength
	# 	indexColon = ContentLength.find(":")
	# 	numContentLength = ContentLength[indexColon+2:]
	# 	# print numContentLength
	# 	findBackrn = numContentLength.find("\r\n")
	# 	pureContentLength = numContentLength[:findBackrn] #now pureContentLength is str type
	# 	print "=========start========="
	# 	# print pureContentLength
	# 	# print "===========End========"
	# 	indexOfrn = data.find("\r\n\r\n")
	# 	body = data[indexOfrn+4:]
		# print body
		# print "------------"
		# print len(data), '-----len data'
		# print len(body),'---------len body'
		# print pureContentLength

		# if int(pureContentLength) == len(body):
		# 	print "download done"
		# sock.close()
		# break
	# if len(data)==0:
	sock.close()
	break



