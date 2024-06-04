import socket
import threading

# Fonction pour gérer les messages reçus d'un client
def handle_client(client_socket):
    while True:
        # Recevoir les données du client
        data = client_socket.recv(1024).decode("utf-8")
        if not data:
            break
        print("Client:", data)

# Configuration du serveur
host = '127.0.0.1'
port = 5555

# Création du socket du serveur
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

print("Server listening on", host, ":", port)

# Attente des connexions des clients
while True:
    client, addr = server.accept()
    print("Connection from", addr)

    # Démarrer un thread pour gérer chaque client
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
 
  