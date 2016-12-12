import subprocess
import signal
import os
import time

# Connect with LE device over hcitool 
#---------------------- Enter here Sensors BLE Address ----------------------------

sensor_address = ['DE:42:D0:A6:71:F2','CD:39:C2:F9:B1:E4']
uart_rx_handle = '0x0b'
uart_tx_handle = '0x0e'

#uart_uuid      = '0000ffe1-0000-1000-8000-00805f9b34fb' 
#notification_handle = '0x12'

class nRF():

	
	def connectLE(self,sensor_address):
		connectSensor = subprocess.Popen(['sudo','hcitool', 'lecc',sensor_address ],stdout=subprocess.PIPE )

		connectionHandle = connectSensor.communicate()[0]		# get the data in tuple
		sensor_con_Handle =  str(connectionHandle)[18:20]
		#print sensor_con_Handle
		return sensor_con_Handle




	def disconnectLE(self, sensor_con_Handle):

		disconnectSensor = subprocess.Popen(['sudo','hcitool','ledc',sensor_con_Handle],stdout=subprocess.PIPE)
		
		print("Disconnecting.....................")
		#output =  disconnectSensor.communicate()
	
		#print (output)



	def read_primary_services(self,sensor_address):
		
		' Method for Primary Service Discovery '

		data = subprocess.Popen(['sudo','gatttool','-b',sensor_address,'--primary'],stdout=subprocess.PIPE )
		
		
		sensor_data =  data.communicate()
		
		print ("Showing Primay Attributes of device : ")
		print (sensor_data)


	def read_by_handle(self,sensor_address,handle):
		
		' Method to Characteristics Value/Descriptor Read by handle '		

		sensor_data = subprocess.Popen(['sudo','gatttool','-b',sensor_address,'--char-read','-a',handle],stdout=subprocess.PIPE)		
		sensor_data = subprocess.Popen(['sudo','gatttool','-i','hci0','-b',sensor_address,'-t','random','-l','low','--char-read','-a',handle],stdout=subprocess.PIPE)
		read_data = sensor_data.communicate()
		
		print(read_data)
	
	def read_by_uuid(self,sensor_address,uuid):

		'Method to Characteristics Value/Descriptor Read by UUIDs'

		#sensor_data = subprocess.Popen(['sudo','gatttool','-b',sensor_address,'--char-read','--uuid='+ uuid],stdout=subprocess.PIPE)
		sensor_data = subprocess.Popen(['sudo','gatttool','-i','hci0','-b',sensor_address,'-t','random','-l','low','--char-read','--uuid='+ uuid],stdout=subprocess.PIPE)        
		get_data = sensor_data.communicate()

		print(get_data)
	
	def listen_Notifications(self,sensor_address,notification_handle):

		'Method to Listen for notifications and indications'
		con_handle = self.connectLE(sensor_address)  		#get connection handle
		print("Connection Handle:",con_handle)		
		self.disconnectLE(con_handle)				# disconnect LE		
		
		time.sleep(2)		
				
		p = subprocess.Popen(['sudo','gatttool','-b',sensor_address,
				      '--char-read','-a', notification_handle,'--listen'],stdout=subprocess.PIPE )
		print("Done Command")
		print(p)
		
		self.disconnectLE(con_handle)		#stop notifications		

		d = p.communicate()

		return d

	def write_by_handle(self,sensor_address,handle,value):
	
		'Method to Characteristics Value Write (Write Request)'	
		
		write_data = subprocess.Popen(['sudo','gatttool','-i','hci0','-b',sensor_address,'-t','random','-l','low','--char-write','-a',handle,'-n',value],stdout=subprocess.PIPE)
		write_res = write_data.communicate()[0]

		print(write_res)


'''	def write_by_uuid(self,sensor_address,handle,value):

		'Not supported to write on UUIDs'
		
                write_data = subprocess.Popen(['sudo','gatttool','-b',sensor_address,'--char-write-req',],stdout=subprocess.PIPE)
                write_res = write_data.communicate()[0]

                print(write_res)

'''



if __name__ == '__main__':

	nRFLE = nRF()		#instance of nRF
	
	#log = open("sensorlog.txt",'a')

	
	try:
	
		#con_handle =nRFLE.connectLE(sensor_address[0])

		#time.sleep(2)
			
		#nRFLE.disconnectLE(con_handle)
		for i in range(0,2):

			nRFLE.write_by_handle(sensor_address[1],uart_tx_handle,value='0x01')
			time.sleep(2)
			
		#nRFLE.read_primary_att(sensor_address[0])
			
		print("Write Complete \n");
		time.sleep(2)
		while True:
	
			nRFLE.read_by_handle(sensor_address[1],uart_rx_handle)
			print("Read Complete \n")
			#nRFLE.read_by_uuid(sensor_address[0],uart_uuid)	
		
			#data = nRFLE.listen_Notifications(sensor_address[0],notification_handle)	
			#nRFLE.write_by_handle(sensor_address[0],uart_handle,value='0x41')

			#log.write(str(data)+'\n')	#log data
	
			time.sleep(2)	
			#nRFLE.disconnectLE(con_handle)
	finally:
	
		print ("Done")
		#log.close()	# close the file


