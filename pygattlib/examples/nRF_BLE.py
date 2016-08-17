#!/usr/bin/python
# -*- mode: python; coding: utf-8 -*-

# Copyright (C) 2016, Vikas Gaikwad <vksgaikwad3@gmail.com>
# This software is under the terms of Apache License v2 or later.

from __future__ import print_function
import sys,time

from gattlib import DiscoveryService
from gattlib import GATTRequester




def scan_LE_devices():

	service = DiscoveryService("hci0")
	devices = service.discover(4)

	for address, name in list(devices.items()):
	    	print("name: {}, address: {}".format(name, address))

	print("Done.")
	return address


class nRF_Connect(object):
    def __init__(self, address):
        self.requester = GATTRequester(address, False)
        self.connect()

    def connect(self):
        print("Connecting...", end=' ')
        sys.stdout.flush()
	#time.sleep(0.5)
        self.requester.connect(True)
        print("OK!")
	#time.sleep(1)

    def request_data(self):			# This will Read data from BLE once it gets connected

     	#data = self.requester.read_by_handle(0x12)[0]    	# 0x12 is UART Service Handle
	data = self.requester.read_by_uuid('0000ffe1-0000-1000-8000-00805f9b34fb')
        print("bytes received:", end=' ')
        for b in data:
            print(hex(ord(b)), end=' ')
        print("")
	print ("Read Complete!!!")
	#time.sleep(0.5)

    def send_data(self):
        self.requester.write_by_handle(0x12, str('A'))	# writing data on UART BLE Service/Notification Handle
	print ("Write Complete!!!")

    def wait_notification(self):
        print("\nThis is a bit tricky. You need to make your device to send\n"
              "some notification. I'll wait...")
        self.received.wait()



	

if __name__ == '__main__':

	
#-------------------- Edit Here Insert Sensors Address ------------------------------
	sensors_list = ['78:A5:04:60:DC:06','78:A5:04:61:23:45']
	UUID = ['0000ffe1-0000-1000-8000-00805f9b34fb']             # place your UUIDs here to read /write
	print ("Length:",len(sensors_list))
	list = scan_LE_devices()		# 

	while(True):

		
		try:
			#for sensor_no in range(0,len(sensors_list)):
			#---------- Read/Write Sensor 1 -----------------------
			time.sleep(0.5)
			#print (" --------------- Sensor 1 ------------------") 
			#nRF_Connect(sensors_list[0]).request_data()
			#time.sleep(2)
			#nRF_Connect(sensors_list[0]).send_data()
		
			#print ("Done with Device No:", sensors_list[0])
	
			#time.sleep(5)
			#--------- Read/Write Sensor 2 --------------------------
			
			print(" ---------- Sensor 2 ---------------")				
			#nRF_Connect(sensors_list[1]).request_data()
			time.sleep(1)
			nRF_Connect(sensors_list[1]).send_data()
			
			print ("Done with Device No :", sensors_list[1])

			time.sleep(5)

		except(RuntimeError,IOError):
			print ("Got Runtime error!!!")
		
