import asyncio
import os

async def receive_file(reader, file_name):
    try:
        file_name = file_name.replace(b'\x00', b'').decode('utf-8').strip()
        file_path = os.path.join(os.path.dirname(__file__), 'files', file_name)

        with open(file_path, "wb") as file:
            while True:
                data = await reader.read(1024)
                if not data:
                    break
                file.write(data)
            print(f"File ricevuto con successo: {file_path}")
    except Exception as e:
        print(f"Errore durante la ricezione del file: {e}")

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f'Nuova connessione da: {addr}')

    try:
        file_name_bytes = await reader.readline()
        await receive_file(reader, file_name_bytes)

    finally:
        print(f'Chiusura della connessione con {addr}')
        writer.close()

async def start_server():
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 8888

    os.makedirs(os.path.join(os.path.dirname(__file__), 'files'), exist_ok=True)

    server = await asyncio.start_server(
        handle_client, SERVER_HOST, SERVER_PORT)

    addr = server.sockets[0].getsockname()
    print(f'Server in ascolto su {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(start_server())
























