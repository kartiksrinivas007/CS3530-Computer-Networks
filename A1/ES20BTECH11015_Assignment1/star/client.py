import socket

cacheIP = "10.0.1.2"

dst_ip = cacheIP #str(input("Enter dstIP: "))
s = socket.socket()

print(dst_ip)

def establish_server_connection(server_ip, port_num):
	server_socket = socket.socket()
	server_socket.connect((server_ip, port_num))
	server_socket.send("Hello Server")
	print ('Client received '+server_socket.recv(1024).decode())
	print("Handshake complete")
	return server_socket

port = 12346

try:
	s = establish_server_connection(cacheIP, port)
	status = True
	while (status == True):
		input_msg = raw_input("Enter your request or enter q to quit\n")
		print("input = ", input_msg)
		if(input_msg == "q"):
			s.send('END /assignment1?request=end HTTP/1.1'.encode())
			status = False
			break
		else:
			print("Sending request  = ", input_msg)
			s.send((input_msg + "\r\n\r\n").encode())
			recv_msg = str(s.recv(1024).decode())
			print("Client received = " + recv_msg)
			continue
	s.close()

except Exception as e:
	print(e)
	print("Error Establishing connection 404")


