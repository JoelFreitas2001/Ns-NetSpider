import os 
from scapy.all import *
import time

class networking:
	print("Hi there i just wanna know the names of your network...")
	time.sleep(2)

	def __init__(self,net):
		self.net = net	

	def pc_name():
		return f(os.name)
	
	def nmap(self):
		try:
			new_window = os.system("start cmd")
		
		save = os.system("nmap -A 192.168.1.1/24")
		
		match save:
			case "Starting Nmap": 

		
