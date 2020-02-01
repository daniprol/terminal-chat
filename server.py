import socket
import time
import pickle




HEADERSIZE = 10

# sockeT.AF_INET = IPv4
# socket.SOCK_STREAM = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# We are going to host the socket so use 'gethostname' to get localhost
# PORT: 1234
s.bind((socket.gethostname(),1234))

s.listen(5) # Leave a queue of 5

while True: #We are going to listen forever!
    clientsocket, address = s.accept()


    print(f"Connection from {address} has been established!")

    d = {1: "Hey", 2: "There"}
    msg = pickle.dumps(d) # This message is already in bytes!!!
    # print(msg)

    # The longest message will be of length 10 digits (1 billion characters)
    # msg = "Welcome to the server!"
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', 'utf-8') + msg # :<10 prints .... until 10 characters
    # print(msg)
    # clientsocket.send(bytes(msg,"utf-8")) # We are sending utf-8 bytes (codified!!!)
    clientsocket.send(msg) # It's already codified!

    # while True:
    #     time.sleep(3)
    #     msg = f"The time is! {time.time()}"
    #     msg = f'{len(msg):<{HEADERSIZE}}' + msg  # :<10 prints .... until 10 characters
    #     clientsocket.send(bytes(msg, "utf-8"))

    clientsocket.close()
    print('Connection has been closed!')
    break
    



