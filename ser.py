import socket
import sys
import urllib2, urllib
import Tkinter
from Tkinter import *
import thread
import netifaces as ni

wlan = 'wlp3s0'
sendto= '192.168.0.106'
sendPort = 7015
listenPort = 7010
ni.ifaddresses(wlan)
HOST = ni.ifaddresses(wlan)[2][0]['addr']
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



top = Tkinter.Tk()

text = Tkinter.Text(top)
text.grid(row=2,column=1)

E1 = Tkinter.Entry(top, bd =5)
E1.grid(row=3,column=1)



def destroysocket():
  s.shutdown(socket.SHUT_RDWR)
  s.close()


def start():
  thread.start_new_thread( listen,("Thread-1", 2, ))
  sendto=B1.get()
  sendPort=int(B2.get())
  listenPort=B3.get()


def send(e):
        
 sock = None
 data = E1.get()
 text.insert(INSERT, HOST+E1.get()+'\n')
      
 E1.delete(0, 'end')
 print "Creating socket"
 sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

 print "Connecting to localhost on port 7010"
 sock.connect((B1.get(), sendPort))
 print "Connection success!"
 
 sock.sendall(data)
 print 'Data sent to server! Now waiting for response...'
   
 del sock




      



def listen(t,d):
    
    # Symbolic name, meaning all available interfaces
   # Arbitrary non-privileged port
 
  
  print 'Socket created'
 
#Bind socket to local host and port
  try:
      s.bind((HOST, sendPort))
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
     
      import subprocess
      subprocess.call(['notify-send','-i','/home/himanshu/Desktop/ico.png',ipv,tail]) 
      


      
 


      print data


B1=Entry(top)
B1.grid(row=1,column=0)
B1.insert(END, 'Send To Ip')

B2=Entry(top)
B2.grid(row=1,column=1)
B2.insert(END, 'Send To Port')

B3=Entry(top)
B3.grid(row=1,column=2)
B3.insert(END, 'Receiving Port')

B4=Button(top, text='Start', command = start)
B4.grid(row=2,column=2)

B5=Button(top, text='destroysocket', command = destroysocket)
B5.grid(row=3,column=2)




E1.bind('<Return>',send)







     





top.mainloop()



	
	


