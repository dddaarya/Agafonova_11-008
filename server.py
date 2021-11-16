import socket

sock = socket.socket()
sock.bind(('localhost', 8080))
sock.listen(1)

conn, addr = sock.accept()

print('connected:', addr)
messages = bytes()

while True:
    data = conn.recv(1024)
    messages += data

    if not data:
        break

    conn.send(data.upper())


conn.close()

print(messages.decode('UTF-8'))