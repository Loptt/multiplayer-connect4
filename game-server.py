import socket
import sys
import threading

class Server:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connections = []
	conn_addresses = []
	max_conns = 2;
	stop_server = False

	host = ""
	port = 5000
	server_address = (host, port)

	def __init__(self):
		try:
			self.s.bind(self.server_address)
			self.s.listen(5)

		except socket.error as e:
			print("Error binding...")
			print(str(e))
			sys.exit()

	def handle_connection(self, conn, conn_address, conn_number):

		while True:

			#Recieve data from one connection
			data = conn.recv(1024) 

			if not data:
				print(str(conn_address[0]) + ":" + str(conn_address[1]) + " dissconnected")
				conn.close()
				self.connections.remove(conn)
				break

			#Forward it to the second connection
			if conn_number == 1:
				self.connections[1].sendall(data)
			else:
				self.connections[0].sendall(data)

	def execute_command(self, command):

		if command == "help":
			print("HELP")

		elif command == "send":
			print("Input message to send all: ")
			message = ("Server says: " + input()).encode()

			for connection in self.connections:
				connection.sendall(message)

		elif command == "stop":
			stop_server = True

			print("Exiting server...")

			try:
				for connection in self.connections:
					connection.close()

				sys.exit()
			except:
				print("Error exiting program...")

			print("Done...")

		elif command == "connections":

			print(" ")
			for number, conn_address in enumerate(self.conn_addresses):
				print("#" + str(number+1) + " -> " +  conn_address)

			print(" ")

		else:
			print("Command " +  command + " not found. Type help for help")
					

	def server_console_manager(self):

		print("For help, type help")

		while True:

			try:
				command = input()
			except:
				print("Data input error")

			self.execute_command(command)




	def run(self):
		print("Initializing server...")
		print("Waiting for connections...\n")

		thread = threading.Thread(target=self.server_console_manager)
		thread.daemon = True
		thread.start()

		while True:
			conn, conn_address = self.s.accept()

			if len(self.connections) > self.max_conns:
				print("Connection to " + str(conn_address[0]) + ":" + str(conn_address[1]) + " refused, max number reached")
				conn.close()
				continue

			thread = threading.Thread(target=self.handle_connection, args=(conn,conn_address,len(self.connections)))
			thread.daemon = True
			thread.start()


			self.connections.append(conn)
			self.conn_addresses.append(str(conn_address[0]) + ":" + str(conn_address[1]))

			print(str(conn_address[0]) + ":" + str(conn_address[1]) + " connected")
			print("Number of connections: " + str(len(self.connections)))

			if self.stop_server:
				break

#START
server = Server()
server.run()

