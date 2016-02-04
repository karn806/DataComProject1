# DataComProject1

when you run srget it will download the link input in this form
  --> srget -o <output file> [-c [<numConn>]] http://someurl.domain[:port]/path/to/file

at first, 
it will check first if the input link is 'https' or not, 
if it is then exit the program
if the link contain no 'http://' then add it in front of the path

then it will check first if the input file name has already existed:
  if it is, then check if the content length of currently download and the existing one is the same
    if it is,  then tell the user that the file has already exited
  if the file has not existed, it will pass to the downloading part

at downloading part:
  i divide the input file into chunk according into number of connection number
  declare starting bytes and ending bytes of each chunk 
  put them into each client and keep these clients into a list
then call asyncore.loop()

after finish downloading those chunks 
i add each data in one variable
then i append that variable into a file with input name

then done! yay

