import socket
import threading

class ChatServer:
    def __init__(self, host="localhost", port=5555):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen()

        self.clients = []
        self.usernames = []

    def broadcast(self, message):
        for client in self.clients:
            client.send(message)

    def handle_connection(self, client):
        while True:
            try:
                message = client.recv(1024)

                if message:
                    self.broadcast(message)

            except:
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                username = self.usernames[index]
                self.usernames.remove(username)
                self.broadcast(f'{username} left the chat!'.encode('utf-8'))
                break

    def start(self):
        while True:
            client, address = self.server.accept()
            print(f"New connection from {address[0]}:{address[1]}")

            client.send('username'.encode('utf-8'))
            username = client.recv(1024).decode('utf-8')
            self.usernames.append(username)
            
            self.clients.append(client)

            print(f"{username} joined the chat!")
            self.broadcast(f"{username} joined the chat!".encode('utf-8'))

            client.send("Connected to the server!".encode('utf-8'))

            client_thread = threading.Thread(target=self.handle_connection, args=(client,))
            client_thread.start()

if __name__ == "__main__":
    server = ChatServer()
    server.start()