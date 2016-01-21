
# create socket
# bind socket
# connect socket
# send request

# open file
# get each piece of info from socket
# write each oiece of info into file
# when done
# readfile and cur off header


import socket as sk 
import os

def mkDownloadRequest(serv, objName):
	return ("GET {o} HTTP/1.1\r\n" + "Host: {s}"+"\r\n\r\n").format(o=objName, s=serv)

#print "{!r}".format(mkDownloadRequest("intranet.mahidol", "/"))

servName = "intranet.mahidol"
port = 80
## create an empty socket
sock = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
## connect to a destination as specified by the pair
sock.connect((servName, port))

request = mkDownloadRequest(servName, "/")
sock.send(request)



def getContentLength(wholeData):
	index = data.find("Content-Length: ")
	# print index
	ContentLength = data[index:]
	#print ContentLength
	indexColon = ContentLength.find(":")
	numContentLength = ContentLength[indexColon+2:]
	# print numContentLength
	findBackrn = numContentLength.find("\r\n")
	pureContentLength = numContentLength[:findBackrn]
	print pureContentLength

def getRidOfHeader(Data):
	if "\r\n\r\n" in Data:
		findrnrnIndex = Data.find('\r\n\r\n')
		sliceHeader = Data[findrnrnIndex+4:]
	print sliceHeader


count = 0
# with open('keepAllData.txt', 'w') as f:
while True:
	data = sock.recv(1024)
	if "Content-Length: " and "\r\n\r\n" in data:
		while count<1:
			ContentLength = getContentLength(data)
			count+=1
	getBody = getRidOfHeader(data)
	if ContentLength == 
	# # write data into txt file
	# with open('keepAllData.txt', 'w') as f:
	# 	f.write(data)

	sock.close
	break














