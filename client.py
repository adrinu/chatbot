import os
import socket
import threading
from server import run_server

# Global Variables 
HOST = "localhost"
PORT = 9999
SERVER_TYPE = ""

def clear_terminal():
    """
    Clears terminal, like performing commands clear or cls (windows)
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def send_message(message):
    """
    Sends message to server

    Args:
        message (str): Text to be sent to server in bytes
    """
    if SERVER_TYPE == "TCP":
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Connects to server
            sock.connect((HOST, PORT))
            
            # Sends the message in bytes
            sock.sendall(bytes(message + "\n", "utf-8"))
            
            # Receives message from server
            recieve_message(sock)
    else:
        # Connects to server
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Sends the message in bytes
        sock.sendto(bytes(message + "\n", "utf-8"), (HOST, PORT))
        
        # Receives messsage from server
        recieve_message(sock)

def recieve_message(sock):
    """
    Receives message from server and outputs to client

    Args:
        sock (socket): Object that represents server connection
    """
    
    # Stores the message received from server
    msg = str(sock.recv(1024))
    
    # Outputs it
    print("ChatBot: {}\n".format(msg.replace("b'", "").replace("'", "")))
        

if __name__ == "__main__":
    greeting_msg = """
 __| |____________________________________________| |__
(__   ____________________________________________   __)
   | |                                            | |
   | |            * Welcome to ChatBot *          | |
   | |      Please enter one of the protocols     | |
   | |          to send your messages over        | |
   | |                                            | |
   | |                  1 - TCP                   | |
   | |                  2 - UPD                   | |
   | |                  3 - Quit                  | |
 __| |____________________________________________| |__
(__   ____________________________________________   __)
   | |                                            | |
"""
    
    # Ask user for choice, repeats if user enters anything else besides 1,2,3
    query = input(greeting_msg +"\n")
    while True:
        if query == "1" or query == "2":
            SERVER_TYPE = "TCP" if query == "1" else "UPD"
            break
        if query == "3":
            clear_terminal()
            print("Didn't want to talk to the ChatBox? What was the point of running this program? You think you cool huh?\n")
            exit()
        
        clear_terminal()
        query = input(greeting_msg + "\n")
    clear_terminal()
    
    # Start the server on a thread
    server = threading.Thread(target=run_server, args=(HOST, int(PORT), SERVER_TYPE), daemon=True)
    server.start()
    
    # User keeps asking the ChatBot until they say bye
    message = input("You: ")
    while message != "Bye!":
        send_message(message)
        message = input("You: ")
    
    
  
    