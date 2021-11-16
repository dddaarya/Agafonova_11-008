import socket

from _thread import *

import threading


print_lock = threading.Lock()

def threaded(c):
    messages = bytes()
    while True:
  
        data = c.recv(1024)
        messages += data

        if not data:
            print_lock.release()
            break
    
        if data.decode('UTF-8').startswith('ThereIsAFile:'):
            some_file_info = data
            some_file = bytes()
            file_weight = some_file_info.decode('UTF-8').split(':')[2]
            file_name = some_file_info.decode('UTF-8').split(':')[1]
            #Получаем файл
            some_file = c.recv(int(file_weight))

            with open(f'server_files/{file_name}', 'wb+') as f:
                f.write(some_file)
        
            continue

        c.send(data.upper())

    c.close()
    print(messages.decode('UTF-8'))


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8080))
sock.listen(5)

while True:
    c, addr = sock.accept()
    print_lock.acquire()

    print('Connected to :', addr[0], ':', addr[1])

    start_new_thread(threaded, (c,))

sock.close()