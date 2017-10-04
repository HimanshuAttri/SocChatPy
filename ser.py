import socket
import sys
import urllib2, urllib
import Tkinter
from Tkinter import INSERT, LEFT,RIGHT,END, re
import thread
import netifaces as ni
ni.ifaddresses('wlp3s0')
HOST = ni.ifaddresses('wlp3s0')[2][0]['addr']


def m1(e):
        
    	 sock = None
         data = E1.get()
         text.insert(INSERT, HOST+data+'\n')
         text.pack()
         E1.delete(0, 'end')
         print "Creating socket"
         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

         print "Connecting to localhost on port 9900"
         sock.connect(('192.168.0.108', 7010))
         print "Connection success!"
 
    	 sock.sendall(data)
    	 print 'Data sent to server! Now waiting for response...'
   
    	 del sock



def fun(t,d):
    
    # Symbolic name, meaning all available interfaces
  PORT = 7010 # Arbitrary non-privileged port
 
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  print 'Socket created'
 
#Bind socket to local host and port
  try:
      s.bind((HOST, PORT))
  except socket.error as msg:
      print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
      sys.exit()
     
  print 'Socket bind complete'
 
#Start listening on socket
  s.listen(10)
  print 'Socket now listening'

 
#now keep talking with the client
  while 1:
    #wait to accept a connection - blocking call
      conn, addr = s.accept()
      print 'Connected with ' + addr[0] + ':' + str(addr[1])
      data= conn.recv(1024)
      tail=data
      print data
      if data =='1001':
         import subprocess
         subprocess.call(['fswebcam','j.jpg']) 

      ipv=addr[0]
      data= addr[0]+": "+data

    
      text.insert(INSERT, data)
      text.pack()
      import subprocess
      subprocess.call(['notify-send','-i','/home/himanshu/Desktop/ico.png',ipv,tail]) 
      


      
 


      print data

     





top = Tkinter.Tk()

E1 = Tkinter.Entry(top, bd =5)

E1.pack(side = RIGHT)
text = Tkinter.Text(top)
text.pack(side = LEFT)

thread.start_new_thread( fun,("Thread-1", 2, ))
E1.bind('<Return>',m1)

top.mainloop()



	
	


