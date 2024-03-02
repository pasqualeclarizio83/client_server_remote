import socket
import threading

# Definisci l'indirizzo IP e la porta su cui il server sarà in ascolto
HOST = '127.0.0.1'  # Indirizzo IP locale
PORT = 65432        # Porta arbitraria non utilizzata

def handle_client(conn, addr):
    print('Connesso a', addr)
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print('Dati ricevuti:', data.decode())
            # Esempio di echo: invia i dati ricevuti indietro al client
            conn.sendall(data)
    print('Connessione con', addr, 'chiusa')

def start_server():
    # Crea un socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Associa il socket all'indirizzo e alla porta desiderati
        server_socket.bind((HOST, PORT))
        # Metti il server in ascolto su un massimo di 5 connessioni in entrata
        server_socket.listen(5)
        print('Server in ascolto...')

        while True:
            # Accetta la connessione
            conn, addr = server_socket.accept()
            # Crea un thread per gestire la connessione
            threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    start_server()