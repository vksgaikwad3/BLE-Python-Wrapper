#!/usr/bin/python

import os,sys
import time
import subprocess
import commands

def scan_LE_devices():
	
	os.system("hciconfig hci0 up")	# Power ON BLE Controller
	time.sleep(1)
	print "Discovering Near by BLE Devices"
        
	devices = os.system("hcitool lescan")	# Retirns the near by BLE devices with its MAC and RSSI value
        
	print "XYZ"
	
	
	#device_list = []
	#for address  in len(devices):
	#	device_list[address]


	#return device_list

def connect_Gatttool(address):
	os.system('gatttool -b '+ address + ' -I')
	time.sleep(3)
	os.system("\n") 

def read_data(address,notify_handle):
	
	print("dads")




if __name__ == '__main__':
	
	

	connect_Gatttool(address = '78:A5:04:61:23:45')
	os.system('connect')


	# commands.getstatusoutput('hcitool lescan')
	
	#subprocess.check_output("hciconfig" + ' ' + "hci0" + ' ' + "up") 	
	#os.system("hciconfig hci0 up")
	#output = subprocess.check_output("hcitool" +' ' + "lescan",shell=True)
	#print 'Have %d bytes in output' % len(output)
	#print output[0]
	#device_list=[]

	#device_info = scan_LE_devices()
	#print 'Bytes %d in '% len(device_info)	

	#print device_list[0]
