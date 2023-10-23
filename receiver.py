import socket
server = socket.socket()
thehost = "10.4.2.72"
hostport = 23992
server.connect((thehost, hostport))


connected = f"I've connected to you!"
message = bytes(connected, 'utf-8')
server.send(message)

print(f"Connection Established")
print(f"IP Addr: {thehost} Port: {hostport}\n")

with open('received_file.txt', 'wb') as writingfile:
    print('Receiving Data')
    while True:
        received_data = server.recv(2048)
        words = str(received_data, 'utf-8')
        print((words))
        if not received_data:
            break
        writingfile.write(received_data)

writingfile.close()
print('File Has Been Received')
server.close()
print('Connection Closing, Goodbye!')
