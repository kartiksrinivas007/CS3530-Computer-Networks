import socket
import time

serverIP = "10.0.1.2"

dst_ip = serverIP #str(input("Enter dstIP: "))
# s = socket.socket()

print(dst_ip)

port = 12346

def establish_server_connection(server_ip, port_num):
	server_socket = socket.socket()
	server_socket.connect((server_ip, port_num))
	server_socket.send("Hello Server")
	print ('Client received '+server_socket.recv(1024).decode())
	print("Handshake complete")
	return server_socket

# s.connect((dst_ip, port))

#Write your code here:
#1. Add code to send HTTP GET / PUT / DELETE request. The request should also include KEY.
#2. Add the code to parse the response you get from the server.
#s.send('GET-key5'.encode())
#s.send('PUT Server'.encode())
# s.send("Hello Server")
#s.send('GET /assignment1?request=key1 HTTP/1.1'.encode())
#s.send('PUT /assignment1?request=key7 val7 HTTP/1.1'.encode())
try:
	s = establish_server_connection(serverIP, port)
	status = True
	while (status == True):
		input_msg = raw_input("Enter your request or enter q to quit\n")
		print("input = ", input_msg)
		if(input_msg == "q"):
			s.send('END /assignment1?request=end HTTP/1.1\r\n\r\n'.encode())
			status = False
			break
		else:
			print("Sending request  = ", input_msg)
			s.send((input_msg + "\r\n\r\n").encode())
			# s.send("PUT /assignment1?request=key7/val7 /HTTP/1.1")
			recv_msg = str(s.recv(1024).decode())
			print("Client received = " + recv_msg)
			continue
	s.close()

except Exception as e:
	print(e)
	print("Error Establishing connection 404")

