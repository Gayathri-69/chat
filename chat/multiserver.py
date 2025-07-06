import socket
import threading

# Constants for the server
HOST = '127.0.0.1'  # Server IP address (localhost)
PORT = 8080  # Server port

# List of connected client sockets
clients = []

# Function to handle communication with a single client
def handle_client(client_socket):
    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024)
            if not message:
                break
            
            # Broadcast the message to all connected clients except the sender
            for client in clients:
                if client != client_socket:
                    client.send(message)
        except ConnectionResetError:
            # If connection is reset, remove client
            break

    # Remove client from the list and close the connection
    clients.remove(client_socket)
    client_socket.close()

# Main function to set up the server
def main():
    # Create server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the server socket to the IP and port
    server_socket.bind((HOST, PORT))
    
    # Listen for incoming connections
    server_socket.listen(5)
    print(f"Server started on {HOST}:{PORT}")

    while True:
        # Accept incoming client connection
        client_socket, client_address = server_socket.accept()
        print(f"Client connected: {client_address}")

        # Add client socket to the list of clients
        clients.append(client_socket)

        # Create a thread to handle communication with the client
        threading.Thread(target=handle_client, args=(client_socket,)).start()

# Run the server
if __name__ == "__main__":
    main()
