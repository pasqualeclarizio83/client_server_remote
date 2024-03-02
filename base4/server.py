import asyncio

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    async def handle_client(self, reader, writer):
        addr = writer.get_extra_info('peername')
        print('Nuova connessione da:', addr)

        try:
            while True:
                data = await reader.readline()
                if not data:
                    print('Connessione interrotta da:', addr)
                    break

                message = data.decode().strip()
                print(f'Ricevuto "{message}" da:', addr)

        finally:
            print(f'Chiusura della connessione con {addr}')
            writer.close()

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



