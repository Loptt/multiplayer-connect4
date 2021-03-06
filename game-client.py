import socket
import threading
import subprocess

class Client:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	message = ""
	server_address = 0
	player_number = 0

	def welcome(self):
		print("Welcome, please enter the address of the connection you want to reach")

		try:
			address = input("Address: ")
			port = input("Port: ")
			print("Connecting to "+address+":"+port+"...")

			return (address, int(port))
		except:
			return ("0.0.0.0",0)

	def send_message(self):

		while True:
			self.message = input("Message: ")
			self.s.sendall(self.message.encode())

			if self.message=="quit":
				break

	def game_process(self):
		subprocess.call(["./connect4"])

	def __init__(self):
		self.server_address = self.welcome()
		thread = threading.Thread(target=self.game_process)
		thread.daemon = True
		thread.start()

	def connect(self):
		try:
			self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.s.connect(self.server_address)
		except:
			print("An error has ocurred")

		#First message recieved from the server is the player number
		self.player_number = self.s.recv(2048).decode()
		subprocess.call(["./writer", player_number])	

		thread = threading.Thread(target=self.send_message)
		thread.daemon = True
		thread.start()

		while True:
			server_message = self.s.recv(2048).decode()

			if not server_message:
				break

			subprocess.call(["./writer",server_message])

			if self.message=="quit":
				break

		self.s.close()


client = Client()
client.connect()