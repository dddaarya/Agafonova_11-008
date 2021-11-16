import socket

# prepare
sock = socket.socket()
sock.connect(('localhost', 8080))

# connection <-> data
msg1 = '— Она мне очень нравится, но я не влюблен в нее.\n'
msg2 = '— А она влюблена в вас, хотя нравитесь вы ей не очень. quit()'


messages = [msg1, msg2]
i = 0

while True:
    message = messages[i]

    sock.send(message.encode('UTF-8')) # ->
    data = bytes()
    
    if len(message.encode('UTF-8')) > 1024:

        while True:
            data += sock.recv(1024)
            
            if len(data) == len(message.encode('UTF-8')):
                break

    else:
        data = sock.recv(1024) # <-

    print(data.decode('UTF-8'))

    if message.find('quit()') != -1:
        break

    i += 1
