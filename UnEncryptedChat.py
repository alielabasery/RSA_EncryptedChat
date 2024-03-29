import sys
import subprocess

try:
    import rsa
except ImportError:
    print("Installing the 'rsa' package...")

    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "rsa"])
        import rsa
    except subprocess.CalledProcessError as e:
        print(f"Error installing 'rsa': {e}")
        sys.exit(1)

import socket
import threading




ip_address = input("Enter the IP address: ")

choice = input ("Do you want to host (1), or to connect (2): ")

if choice == "1" :
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((ip_address, 9999))
        server.listen()

        client, _ = server.accept()

elif choice == "2" : 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip_address, 9999))

else:
    exit()


def sending_messages(c):
    while True:
        message = input("")
        c.send(message.encode())
        print("You: " + message)


def receiving_messages(c):
    while True:
        print("Partner: " + c.recv(1024).decode())


threading.Thread(target=sending_messages, args=(client, )).start()
threading.Thread(target=receiving_messages, args=(client, )).start()
