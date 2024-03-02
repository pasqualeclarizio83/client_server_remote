import asyncio

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = []

    async def handle_client(self, reader, writer):
        self.clients.append(writer)
        addr = writer.get_extra_info('peername')
        print('Nuova connessione da:', addr)

        while True:
            data = await reader.read(100)
            message = data.decode()
            if not message:
                print('Connessione interrotta da:', addr)
                self.clients.remove(writer)
                break

            print(f'Ricevuto "{message}" da:', addr)

            # Esempio di echo: invia il messaggio a tutti i client tranne a chi lo ha inviato
            for client in self.clients:
                if client != writer:
                    client.write(data)
                    await client.drain()

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
