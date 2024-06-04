import socket
import threading

# Configuration du client
host = '127.0.0.1'
port = 5555

# Création du socket du client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# Fonction pour envoyer les messages au serveur
def send_message():
    while True:
        message = input()
        client.send(message.encode("utf-8"))

# Démarrer un thread pour envoyer les messages
send_thread = threading.Thread(target=send_message)
send_thread.start()

# Attendre les messages du serveur et les afficher
while True:
    response = client.recv(1024).decode("utf-8")
    print("Server:", response)
