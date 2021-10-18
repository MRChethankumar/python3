fhandler = open("file.txt", "w")
fhandler.write("From xyz.vhy@perfectplanb.net Sat Jan 5 09:14:16 2008. Return-Path: Received: from murder (perfectplanb.net [141.211.14.90]) by mail.perfectplanb.net with LMTPA;Sat, 05 Jan 2008 09:14:16 -0500")
fhandler.close()

fhandler = open("file.txt", "r")
for line in fhandler:
    print(line.rstrip().upper())

fhandler.close()

