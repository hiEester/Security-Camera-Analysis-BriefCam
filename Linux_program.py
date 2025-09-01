
import os
from socket import *
from PIL import Image
from base64 import b64encode
import base64 
import configparser
import subprocess

config=configparser.ConfigParser()
config.read("configuration.yaml")
host = "192.168.103.32" # set to IP address of target computer
port = 10000
addr = (host, port)
#
UDPSock = socket(AF_INET, SOCK_DGRAM)
count_first=0
count_secend=config.getint("BIT","number")
#result=os.system("raspistill -o imgtest.jpeg")
#print(result)
#result = subprocess.check_output(img, shell=True)


folder_dir = "/home/aaa/project/images"
for images in os.listdir(folder_dir):
# open method used to open different extension image file
	while True:
      #image = open('/home/aaa/project/img1.png', 'rb') #open binary file in read mode
		image = open(folder_dir+'/'+images, 'rb')
		image_read = image.read()
		image_64_encode = base64.b64encode(image_read)
      #print (image_64_encode)
		UDPSock.sendto(image_64_encode[count_first:count_secend], addr)
		if count_secend >= len(image_64_encode):
			finish_img="finish img"
			UDPSock.sendto(finish_img.encode(),addr)
			count_first=0
			count_secend=config.getint("BIT","number")
			break
		count_first=  count_first+config.getint("BIT","number")
		count_secend=count_secend+config.getint("BIT","number")
   #   data = input("Enter message to send or type 'exit': ")
   #   UDPSock.sendto(data.encode(), addr)
exit="exit"     
UDPSock.sendto(exit.encode(),addr)
UDPSock.close()
os._exit(0)


