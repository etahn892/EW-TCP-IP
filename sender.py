import socket
ethansport = 23992
server = socket.socket()
ethanspc = "10.4.2.72"
server.bind((ethanspc, ethansport))
server.listen()
print('Server Open For Connections')
count = 1
while True:
    connection, addr = server.accept()
    print(f'Successfull Connection From {addr}')
    print(f"IP Addr: {addr[0]} Port: {addr[1]}")
    received_data = connection.recv(2048)
    received_data = str(received_data, 'utf-8')
    print(f'{addr} Says: "{received_data}"')

    file ='TCP-IP-TestFile.txt'
    fh = open(file, 'r')
    reading = fh.read(2048)
    if reading:
        pass
    while reading:
        reading = bytes(reading, 'utf-8')
        connection.send(reading)
        print(f'Data Sent {count}')
        count += 1
        reading = fh.read(2048)
    fh.close()

    print('All Data Has Been Sent')
    connection.close()
