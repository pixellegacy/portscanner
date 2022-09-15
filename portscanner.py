#!/bin/python3

import sys
import socket
from datetime import datetime 

#define our target
if len(sys.argv) ==2:
     target=socket.gethostbyname(sys.argv[1]) #translate hostname in to ip by dns
else:
  print("invalid argumant")
  print(" syntax: scanner.py <ip>")
  
#banner 
print("-" *50)
print("scanning target " + target)
print("scanning started:"+ str(datetime.now()))

#port scanning
try:
   for port in range(1,1000):
      s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      socket.setdefaulttimeout(1)
      result=s.connect_ex((target,port)) #return an error indication
   if result==0:
        print("port {} is open".format(port))
   s.close()
   
except KeyboardInterrupt:
         print("\n exiting program.")
         sys.exit()
         
except socket.gaierror:
       print("Hostname is not resolve")
       sys.exit()
except socket.error:
       print("could not connect to server")
       sys.exit()
     #python3 scanner.py <ip> 
