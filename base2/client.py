import socket

# Definisci l'indirizzo IP e la porta del server a cui connettersi
SERVER_HOST = '127.0.0.1'  # Indirizzo IP del server
SERVER_PORT = 65432        # Porta su cui il server è in ascolto

# Messaggio da inviare al server
message = "Ciao, server!"

# Crea un socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Connetti il client al server
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    # Invia il messaggio al server
    client_socket.sendall(message.encode())
    # Ricevi la risposta dal server
    data = client_socket.recv(1024)

print('Ricevuto:', data.decode())