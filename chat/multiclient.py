import socket
import threading

# Constants for the client
HOST = '127.0.0.1'  # Server IP address (localhost)
PORT = 8080  # Server port

# Function to receive and display messages from the server
def receive_messages(client_socket):
    while True:
        try:
            # Receive message from the server
            message = client_socket.recv(1024)
            if not message:
                break
            # Print the received message
            print(message.decode())
        except ConnectionResetError:
            break

# Main function to set up the client
def main():
    # Create client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    client_socket.connect((HOST, PORT))
    print(f"Connected to server on {HOST}:{PORT}")

    # Create a thread to receive and display messages from the server
    threading.Thread(target=receive_messages, args=(client_socket,)).start()

    while True:
        # Get message input from the user
        message = input()
        if message:
            # Send the message to the server
            client_socket.send(message.encode())

# Run the client
if __name__ == "__main__":
    main()
