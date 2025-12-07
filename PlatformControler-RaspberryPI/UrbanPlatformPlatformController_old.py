import socket

import smbus
import time
import sys

def SendToArd(message, arduAddress):
    for c in list(message):
        # send data
        bus.write_byte(arduAddress,c)
        print(bus.read_byte(arduAddress))

    

bus = smbus.SMBus(1)
arduAddress1 = 0x04              # Arduino I2C Addresses
arduAddress2 = 0x05
arduAddress3 = 0x06

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 12000))

i2cData = 25


while True:
    message, address = server_socket.recvfrom(1024)
    message = message.upper()
    
    print("from GUI:" + str(message))
    
    SendToArd(message, arduAddress1)
    
    #print ("Arduino 1 answer to RPi:", bus.read_byte(arduAddress1))
    #print ("Arduino 2 answer to RPi:", bus.read_byte(arduAddress2))
    #print ("Arduino 3 answer to RPi:", bus.read_byte(arduAddress3))

    server_socket.sendto(message, address)
