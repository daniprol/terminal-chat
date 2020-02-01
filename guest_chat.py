import socket
import select
import errno # Matches specific error codes
import sys


##### THIS GUEST VERSION OF THE CLIENT IS ONLY ALLOWED TO READ MESSAGES FROM THE SERVER!!!!!!
# What the client does is telling the server its username.
# From there we do an infinite loop trying to send and receive messages.

HEADER_LENGTH = 10

IP = '127.0.0.1'
PORT = 1234

my_username = input("Username: ")
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)  # This way the received functionality won't be blocking

username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')

client_socket.send(username_header + username)

while True:
    # message = input(f"{my_username} > ") # We are not allowed to send messages!!
    message = ''

    # If you accidentally press enter:
    if message:
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')

        client_socket.send(message_header + message)
    try: # We are expecting an error at some point for sure!
        while True:
            # Receive things:
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print("Connection closed by the server")
                sys.exit()

            username_length = int(username_header.decode('utf-8').strip())
            username = client_socket.recv(username_length).decode('utf-8')

            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')

            print(f"{username} > {message}")
    except IOError as e:
        # Errors depending on the operating system when there are no more messages to be received
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error', str(e))
            sys.exit()

        continue # If it was an errno.EAGAIN  or errno.EWOULDBLOCK we want to continue with the chat


    except Exception as e:
        print('General error', str(e))
        sys.exit()

