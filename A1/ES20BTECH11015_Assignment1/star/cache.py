import socket

cache_dict ={"key1":  "val1", 
 }
print("the cache dictionary is = ", cache_dict)

dst_ip = "10.0.1.2"#str(input("Enter Server IP: "))
server_ip = "10.0.1.3"

s = socket.socket()
print ("Socket successfully created")

dport = 12346
port_num = dport # will this cause issues ? 

s.bind((dst_ip, dport))
print ("socket binded to %s" %(dport))

s.listen(5)
print ("socket is listening")


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

def establish_server_connection(server_ip, port_num):

  """
  establish connection to the Main server and complete
  a Handshake
  """

  server_socket = socket.socket()
  server_socket.connect((server_ip, port_num))
  server_socket.send("Hello Server")
  recv_server = server_socket.recv(1024).decode()
  return server_socket


# def parse_cache(recv_string,c,cache_dict):

#   if(recv_string[:3] == "GET"):

#     """
#      If the request is a GET request then first check if the key exists in the cached dictionary and then
#      return, else establisha  connection to the server and then forward the request to the server
#     """
    
#     print("GET request received")
#     list_string = recv_string.split("request=")
#     print(list_string)
#     key_http = list_string[1].split(' ')
#     print(key_http)
#     key = key_http[0]
#     if(cache_dict.has_key(key)):
#       c.send("The value of the key sent = " + cache_dict[key])
#     else:  
#       server_socket  = establish_server_connection(server_ip,port_num)
#       server_socket.send(recv_string.encode())
#       recv_server = str(server_socket.recv(1024).decode())
#       print("Received from server = ", recv_server)
#       c.send("From Server -> Cache -> Client  = " + recv_server)
#   elif(recv_string[:3] == "PUT"):

#     """simply forward the PUT request to the Server and 
#     get the received string back """

#     print("PUT request received")
#     server_socket = establish_server_connection(server_ip, port_num)
#     server_socket.send(recv_string.encode())
#     recv_server = str(server_socket.recv(1024).decode())
#     print("Received from server = ", recv_server)
#     c.send("From Server -> Cache -> Client" + recv_server)


#   elif(recv_string[:6] == "DELETE"):

#     """simply forward the DELETE request to the Server and 
#     get the received string back """

#     print("DELETE request received")
#     server_socket = establish_server_connection(server_ip, port_num)
#     server_socket.send(recv_string.encode())
#     recv_server = str(server_socket.recv(1024).decode())
#     print("Received from server = ", recv_server)
#     c.send("From Server -> Cache -> Client" + recv_server)
#     ### cache deletion tbd
#   else:
#     #END request is needed
#     #parsing should be similar to server.py
#     print("Unable to parse request")


def parse_cache(recv_string,c,server_dict):

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
    if(cache_dict.has_key(key)):
      to_return = cache_dict[key]
      c.send(("HTTP/1.1 200 OK " + to_return + "\r\n\r\n").encode())
      return True
    else:
      try:
        print('Cache Does not have Key!, Sending Request to server')
        server_socket  = establish_server_connection(server_ip,port_num)
        server_socket.send(recv_string.encode())
        recv_server = str(server_socket.recv(1024).decode())
        http_value_carriage = recv_server.split("OK")
        value = http_value_carriage[1].strip()
        # print("value of requested key = ", value)
        cache_dict[key] = value
        print("Cache Dictionary updated due to recent request = ", cache_dict)
        server_socket.send('END /assignment1?request=end HTTP/1.1'.encode())
        print("Received from server = ", recv_server)
        c.send((recv_server + "\r\n\r\n").encode())

      except:
        print("Error establishing connection To server from the Cache")
        return False
    # try:
    #   to_return = cache_dict[key]
    #   c.send(to_return.encode())
    #   return True
    # except:
    #   c.send("Error 404 Key Not Found")
    #   return False
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

    #-------
    try:
      server_socket  = establish_server_connection(server_ip,port_num)
      server_socket.send(recv_string.encode())
      recv_server = str(server_socket.recv(1024).decode())
      server_socket.send('END /assignment1?request=end HTTP/1.1\r\n\r\n'.encode())
      print("Received from server = ", recv_server)
      c.send((recv_server + "\r\n\r\n").encode())
      cache_dict[key] = value
      print("updated dictionary = ", cache_dict)
      return True
    except:
      print("Error establishing connection To server from the Cache")
      return False
    #------


  elif(recv_string[:6] == "DELETE"):
    print("DELETE request received")
    # list_string = recv_string.split("request=")
    # print(list_string)
    # key_http = list_string[1].split(' ')
    # print(key_http)
    # key = key_http[0]
    list_string = recv_string.split(" ")
    file_path = list_string[1]
    print('File path = ', file_path)
    key = file_path.split("/")[2]
    print("key=",  key)

    try:
      server_socket  = establish_server_connection(server_ip,port_num)
      server_socket.send(recv_string.encode())
      recv_server = str(server_socket.recv(1024).decode())
      server_socket.send('END /assignment1?request=end HTTP/1.1\r\n\r\n'.encode())
      print("Received from server = ", recv_server)
      c.send(("HTTP/1.1 200 OK From Server -> Cache -> Client  = " + recv_server + "\r\n\r\n").encode())
      if(cache_dict.has_key(key)):
        del cache_dict[key]
        print("Successful delete on the cache")
        print("Updated Dictionary = ", cache_dict)
      else:
        print("Cache does not Have this Key anyways")
      return True
    except:
      print("Error establishing connection To server from the Cache")
      return False


    # try:
    #   del server_dict[key]
    #   print("Successful Delete")
    #   c.send("200 OK")
    #   print("updated dictionary = ", server_dict)
    #   return True
    # except:
    #   print("Failed DELETE Request")
    #   c.send("404 Key Not Found")
    #   return False

  elif(recv_string[:3] == "END"):
    print("Ending Connection")
    c.send("Ending Connection")
    return False
  else:
    c.send("HTTP/1.1 400 Bad Request \r\n\r\n")
    print("Unable to parse request from connection, connection closed")
    return False



while True:
#here c is the connection
  # c, addr = s.accept()
  # print ('Got connection from', addr )
  # recvmsg = c.recv(1024).decode()
  # print('Server received '+recvmsg)
  # c.send('Hello client'.encode())'---'
  # c, addr = establish_client_connection(s)

  # recvmsg = c.recv(1024).decode()
  # print("type of received message = ", type(recvmsg))
  # recv_string = str(recvmsg)
  # print("received message in string format = ", recv_string)
  # parse_cache(recv_string,c,cache_dict)
  #---
  status = False
  try:
     c, addr = establish_client_connection(s)
     status = True
     while(status == True):  
       recvmsg = c.recv(1024).decode()
       print("type of received message = ", type(recvmsg))
       recv_string = str(recvmsg)
       print("received message in string format = ", recv_string)
       status = parse_cache(recv_string,c,cache_dict)
       #send END request to server post caching? #return sever socket and then we will end connection together?
     print("Connection Ended with ", addr)
     print("Waiting for New connection")
  except:
    print("Ending Server Session Due to Keyboard-IP or error")
    break
  
  #Write your code here
  #1. Uncomment c.send 
  #2. Parse the received HTTP request
  #3. Do the necessary operation depending upon whether it is GET, PUT or DELETE
  #4. Send response
  ##################

  c.close()
  #break
