import socket 

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('postman-echo.com', 80) 
client_socket.connect(server_address)

request = "POST /post HTTP/1.1\r\nHost: postman-echo.com\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 16\r\n\nname=Paul&age=27"
client_socket.send(request.encode())  

response = client_socket.recv(4096) 
print("Response from server:")
print(response.decode())  

client_socket.close()