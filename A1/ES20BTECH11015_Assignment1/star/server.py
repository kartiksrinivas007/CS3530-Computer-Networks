

import socket

#WRITE CODE HERE:
#1. Create a KEY-VALUE pairs (Create a dictionary OR Maintain a text file for KEY-VALUES).

server_dict ={"key1":  "val1", 
"key2":  "val2",
"key3":  "val3",
"key4":  "val4",
"key5":  "val5",
"key6":  "val6",
 }
print("the server dictionary is = ", server_dict)

dst_ip = "10.0.1.3"#str(input("Enter Server IP: "))

s = socket.socket()
print ("Socket successfully created")

dport = 12346

def establish_client_connection(server_socket):

  """
  This function establishes a connection with the client through the particular socket
  on a server, it returns the connection and the address
  """
  c, addr = server_socket.accept()
  print ('Got connection from', addr )
  recvmsg = c.recv(1024).decode()
  print('Server received '+recvmsg)
  c.send('Hello client'.encode())
  return c, addr

s.bind((dst_ip, dport))
print ("socket binded to %s" %(dport))

s.listen(5)
print ("socket is listening")

def parse(recv_string,c,server_dict):

  """
    This function parses the received request and then csends a response to the 
    client through the connection c
  """

  if(recv_string[:3] == "GET"):
    print("GET request received")
    list_string = recv_string.split("request=",)
    print(list_string)
    key_http = list_string[1].split(' ')
    print(key_http)
    key = key_http[0]
    try:
      to_return = server_dict[key]
      c.send("HTTP/1.1 200 OK " + to_return + "\r\n\r\n".encode())
      return True
    except:
      c.send("HTTP/1.1 404 Key Not found \r\n\r\n")
      return False
  elif(recv_string[:3] == "PUT"):
    print("PUT request received")
    # list_string = recv_string.split("request=")
    # print(list_string)
    # key_value_http = list_string[1].split(' ')
    # print(key_value_http)
    # key_value = key_value_http[0].split('/')
    # print(key_value)
    # key = key_value[0]
    # value = key_value[1]
    list_string = recv_string.split(" ")
    file_path = list_string[1]
    print("File path = ", file_path)
    key = file_path.split("/")[2]
    value = file_path.split("/")[3]
    print(key, value)
    server_dict[key] = value
    c.send("HTTP/1.1 200 OK\r\n\r\n")
    print("updated dictionary = ", server_dict)
    return True

  elif(recv_string[:6] == "DELETE"):
    print("DELETE request received")
    list_string = recv_string.split(" ")
    file_path = list_string[1]
    print('File path = ', file_path)
    key = file_path.split("/")[2]
    print("key=",  key)
    try:
      del server_dict[key]
      print("Successful Delete")
      c.send("HTTP/1.1 200 OK\r\n\r\n")
      print("updated dictionary = ", server_dict)
      return True
    except:
      print("Failed DELETE Request")
      c.send("HTTP/1.1 404 Key Not Found\r\n\r\n")
      return False

  elif(recv_string[:3] == "END"):
    print("Ending Connection")
    c.send("Ending Connection")
    return False
  else:
    c.send("HTTP/1.1 400\r\n\r\n")
    print("Unable to parse request from connection, connection closed")
    return False


  

while True:
#here c is the connection

  """
   I am trying to implement a persistent HTTP model, which will perform 
   multiple HTTP requests one by one over the same  connection
   END will kill the connection between client and server, once received
  """
  
  status = False
  try:
     c, addr = establish_client_connection(s)
     status = True
     while(status == True):  
       recvmsg = c.recv(1024).decode()
       print("type of received message = ", type(recvmsg))
       recv_string = str(recvmsg)
       print("received message in string format = ", recv_string)
       status = parse(recv_string,c,server_dict)
     print("Connection Ended with ", addr)
     print("Waiting for New connection")
  except:
    print("Ending Server Session Due to Keyboard-IP or error")
    break
    """
    Only if we get an error will we enter the except block 
    it will not automatically go there
    """

  c.close()
  #break
