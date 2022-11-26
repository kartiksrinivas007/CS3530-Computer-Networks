import socket
import sys
import time 

senderIP = "10.0.0.1"
senderPort   = 20001
recieverAddressPort = ("10.0.0.2", 20002)
bufferSize  = 1024 #Message Buffer Size
timeout_time = 1e-5

# Create a UDP socket at reciever side
socket_udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
img = open('testFile.jpg', 'rb').read()
print(img)
# for i in range(0, len(data), bufferSize):
#     rdt_send(data[i:i+bufferSize])

# print(1.2 *1024 * 1024/len(Temp))  # approximately equal to one


# def rdt_send(c, state = 0):
# 	if(status == 0):
# 		socket.sendto(c, recieverAddressPort)
# 		time_sent = time.time()
# 		#wait for reply from server
# 		if(time.time() - time_sent > timeout_time):
# 			pass

# print(Temp[0:512])

# while True:
# 	rdt_send(Temp[0:512])


while True:

    # Send to server using created UDP socket
    msg = input("Please enter message to send: ")
    message = str.encode(msg)
    socket_udp.sendto(message, recieverAddressPort)

    #wait for reply message from reciever
    msgFromServer = socket_udp.recvfrom(bufferSize)

    msgString = "Message from Server {}".format(msgFromServer[0])
    print(msgString)
