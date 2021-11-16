import socket

some_file = bytes()
#Чтобы передать файл нужно отправить два сообщения:
#1)"ThereIsAFile:<название файла>:<вес файла>"
#2)Сам файл

file = open('15884504933310.jpg', 'rb').read()
file_info = f"ThereIsAFile:15884504933310.jpg:{len(file)}"

# prepare
sock = socket.socket()
sock.connect(('localhost', 8080))

# connection <-> data
msg1 = '— Нынешние молодые люди воображают, что деньги это всё.'
msg2 = '— … А с годами они в этом убеждаются. quit()'

messages = [msg1, file_info, file, msg2,]
i = 0
next_message_is_file = False

while True:
    message = messages[i]
    data = bytes()

    if next_message_is_file:
        sock.send(message)
        next_message_is_file = False
        i += 1
        continue

    else:
        sock.send(message.encode('UTF-8'))

    if message.startswith('ThereIsAFile'):
        next_message_is_file = True
    

    if len(message.encode('UTF-8')) > 1024:

        while True:
            if not next_message_is_file:
                data += sock.recv(1024)
            
            if len(data) == len(message.encode('UTF-8')):
                break

    else:
        if not next_message_is_file:

            data = sock.recv(1024) # <-
            print(data.decode('UTF-8'))

    if message.find('quit()') != -1:
        break

    i += 1
