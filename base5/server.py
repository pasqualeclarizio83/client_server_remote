import asyncio

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = []

    async def handle_client(self, reader, writer):
        addr = writer.get_extra_info('peername')
        print(f'Nuova connessione da: {addr}')

        try:
            self.clients.append(writer)

            while True:
                data = await reader.readline()
                message = data.decode().strip()

                if message.lower() == 'exit':
                    print(f'{addr} ha interrotto la connessione.')
                    break

                print(f'Ricevuto da {addr}: {message}')

                # Rispondi al client
                response = input("Inserisci la risposta da inviare al client: ")
                await self.send_message(response)

        finally:
            print(f'Chiusura della connessione con {addr}')
            writer.close()
            self.clients.remove(writer)

    async def send_message(self, message):
        # Invia il messaggio a tutti i client
        for writer in self.clients:
            writer.write(message.encode() + b'\n')
            await writer.drain()

    async def start_server(self):
        server = await asyncio.start_server(
            self.handle_client, self.host, self.port)

        addr = server.sockets[0].getsockname()
        print(f'Server in ascolto su {addr}')

        async with server:
            await server.serve_forever()

if __name__ == "__main__":
    server = Server('127.0.0.1', 8888)
    asyncio.run(server.start_server())



















