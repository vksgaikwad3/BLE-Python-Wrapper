import subprocess
import signal
import os
import time

# Connect with LE device over hcitool 
#---------------------- Enter here Sensors BLE Address ----------------------------

sensor_address = ['78:A5:04:61:23:45']
uart_handle = '0x12'
#uart_tx_handle = '0x12'
uart_uuid      = '0000ffe1-0000-1000-8000-00805f9b34fb' 
notification_handle = '0x12'

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



	def read_primary_services(self,sensor_address):
		
		data = subprocess.Popen(['sudo','gatttool','-b',sensor_address,'--primary'],stdout=subprocess.PIPE )

		
		sensor_data =  data.communicate()
		
		print ("Showing Primay Attributes of device : ")
		print (sensor_data)


	def read_by_handle(self,sensor_address,handle):
		
		sensor_data = subprocess.Popen(['sudo','gatttool','-b',sensor_address,'--char-read','-a',handle],stdout=subprocess.PIPE)		
		read_data = sensor_data.communicate()
		
		print(read_data)
	
	def read_by_uuid(self,sensor_address,uuid):

                sensor_data = subprocess.Popen(['sudo','gatttool','-b',sensor_address,'--char-read','--uuid='+ uuid],stdout=subprocess.PIPE)
                get_data = sensor_data.communicate()

                print(get_data)
	
	def listen_Notifications(self,sensor_address,notification_handle):
		
		p = subprocess.Popen(['sudo','gatttool','-b',sensor_address,'--char-read','-a', notification_handle,'--listen'],stdout=subprocess.PIPE )
		print("Done Command")
		
		d = p.communicate()
		print ("Done Communicate")

		print(p)
		os.kill(d.pid, signal.SIGINT)
		print("Killed")



	def write_by_handle(self,sensor_address,handle,value):
	
		write_data = subprocess.Popen(['sudo','gatttool','-b',sensor_address,'--char-write-req','-a',handle,'-n',value],stdout=subprocess.PIPE)
                write_res = write_data.communicate()[0]

                print(write_res)


	def write_by_uuid(self,sensor_address,handle,value):

                write_data = subprocess.Popen(['sudo','gatttool','-b',sensor_ad$
                write_res = write_data.communicate()[0]

                print(write_res)





if __name__ == '__main__':

	nRFLE = nRF()		#instance of nRF

	#con_handle =nRFLE.connectLE(sensor_address[0])

	time.sleep(2)
	#nRFLE.read_primary_att(sensor_address[0])
	#nRFLE.read_by_handle(sensor_address[0],uart_handle)
	#nRFLE.read_by_uuid(sensor_address[0],uart_uuid)	
	#nRFLE.listen_Notifications(sensor_address[0],notification_handle)	
	nRFLE.write_by_handle(sensor_address[0],uart_handle,'0x41')


	#nRFLE.disconnectLE(con_handle)
	print ("Done")


