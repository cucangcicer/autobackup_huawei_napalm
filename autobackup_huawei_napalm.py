from napalm import get_network_driver
import os
import sys
import datetime

x = datetime.datetime.now()
collection_time = x.strftime("%y")+x.strftime("%m")+x.strftime("%d")+"-"+x.strftime("%H")+x.strftime("%M")+x.strftime("%S")
file_directory = "./Backup/"
file = open("device_list.txt","r") #Device list 
host_list = file.read().split()

user = 'mandiri' #Specify user login here
user_pswd = 'P@ssw0rd' #Specify user password here
ssh_port = 22 #Specify ssh port here
running_config = ""

for host in host_list:
	try:
		#Establishing connection
		driver = get_network_driver('huawei_vrp')
		device = driver(hostname = host, username = user, password = user_pswd, optional_args = {'port':ssh_port})
		device.open()
		send_command = device.cli(['n \n'])
		#Hostname collect
		command_output = device.get_facts()
		hostname = command_output["hostname"]
		#Configuration collect
		command_output = device.cli(['dis current'])
		running_config = command_output["dis current"]
	except:
		#Put exception error here
		print("Collection Error!")
		#continue
	#Creating configuration file
	file_dir = file_directory+hostname+"_"+collection_time
	conf_file = open("{}.txt".format(file_dir),"w")
	conf_file.write(running_config)
	conf_file.close()
	device.close()
file.close()
