import threading
import socket

alias = input("Choose an alias =>>")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 50000))

def client_receive():
    while True:
        try:
            mess = client.recv(1024).decode('utf-8')
            if mess == "alias?":
                client.send(alias.encode('utf-8'))
            else:
                print(mess)
        except Exception as e:
            print(f'An error occurred: {e}')
            client.close()
            break

def client_send():
    while True:
        mess = f'{alias}: {input("")}'
        client.send(mess.encode('utf-8'))

receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()