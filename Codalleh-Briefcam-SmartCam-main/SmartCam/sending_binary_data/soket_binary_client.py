# import binascii
# import socket
# import struct
# import sys
#
# # Create a TCP/IP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_address = ("192.168.80.137", 10000)
# sock.connect(server_address)
#
# values = (1, 'ab', 2.7)
# packer = struct.Struct('I 2s f')
# packed_data = packer.pack(*values)
#
# try:
#
#     # Send data
#     print('sending "%s"' % binascii.hexlify(packed_data), values,file=sys.stderr)
#     #print >> sys.stderr, 'sending "%s"' % binascii.hexlify(packed_data), values
#     sock.sendall(packed_data)
#
# finally:
#     print('closing socket', values, file=sys.stderr)
#     #print >> sys.stderr, 'closing socket'
#     sock.close()

# import os
# from socket import *
#
# host = "192.168.80.137" # set to IP address of target computer
# port = 10000
# addr = (host, port)
#
# UDPSock = socket(AF_INET, SOCK_DGRAM)
#
# while True:
#     data = input("Enter message to send or type 'exit': ")
#     UDPSock.sendto(data.encode(), addr)
#     if data == "exit":
#         break
#
# UDPSock.close()
# os._exit(0)
import base64
import os
from socket import *
import io
from PIL import Image
def get_image():
    host = "192.168.103.32"
    port = 10000
    buf = 1024

    address = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    UDPSock.bind(address)
    all_data=""
    print ("Waiting to receive messages...")
    count=0
    while True:
        (data, address) = UDPSock.recvfrom(buf)
        print("Received message: " + data.decode())
        print(count)
        if data.decode() == "exit":
            break
        if data.decode()=="finish img":
            img = base64.b64decode(all_data)
            image = io.BytesIO(img)
            imageFile = Image.open(image)
            imageFile.show()
            path="C:/Users/213330962/project/images/"
            imageFile.save(path+"img"+str(count) +".png")
            count=count+1
            all_data=""
            continue
        all_data = all_data + data.decode()
    UDPSock.close()
    return path