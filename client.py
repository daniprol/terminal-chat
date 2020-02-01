import socket
import pickle
HEADERSIZE = 10
# sockeT.AF_INET = IPv4
# socket.SOCK_STREAM = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# The client is going to use the SAME EXACT SOCKET!!

s.connect((socket.gethostname(),1234))

print('Welcome to the server!')
while True: # We use while loop to continuously buffer data!

    full_msg = b''
    new_msg = True

    while True:
        msg = s.recv(16)
        if new_msg :
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[0:HEADERSIZE])
            new_msg = False

        # full_msg += msg.decode("utf-8")
        full_msg += msg

        if len(full_msg) - HEADERSIZE == msglen:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])

            d = pickle.loads(full_msg[HEADERSIZE:])
            print(d)
            new_msg = True
            full_msg = b''

    print(full_msg)