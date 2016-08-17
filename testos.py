import subprocess
import os
import time

# Connect with LE device over hcitool 
#---------------------- Enter here Sensors BLE Address ----------------------------

sensor_address = ['78:A5:04:61:23:45']
uart_rx_handle = '0x12'
uart_tx_handle = '0x12'
uart_uuid      = '0000ffe1-0000-1000-8000-00805f9b34fb' 

class nRF():

	
	def connectLE(self,sensor_address):
		connectSensor = subprocess.Popen(['sudo','hcitool', 'lecc',sensor_address ],stdout=subprocess.PIPE )

		connectionHandle = connectSensor.communicate()[0]		# get the data in tuple
		sensor_con_Handle =  str(connectionHandle)[18:20]
		#print sensor_con_Handle
		return sensor_con_Handle




	def disconnectLE(self, sensor_con_Handle):

		disconnectSensor = subprocess.Popen(['sudo','hcitool','ledc',sensor_con_Handle],stdout=subprocess.PIPE)

		output =  disconnectSensor.communicate()
	
		print (output)



	def read_by_handle(self,sensor_address):
		
		data = subprocess.Popen(['sudo','gatttool','-b',sensor_address,'--char-read', '--hdle=0x12', '--listen'],stdout=subprocess.PIPE )

		sensor_data =  data.communicate()
		print (sensor_data)

		
		
		

if __name__ == '__main__':

	nRFLE = nRF()		#instance of nRF

	con_handle =nRFLE.connectLE(sensor_address[0])

	time.sleep(2)
	nRFLE.read_by_handle(sensor_address[0])

		
	nRFLE.disconnectLE(con_handle)
	print ("Done")


