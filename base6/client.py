import asyncio
import os

async def send_file(reader, writer, file_path):
    try:
        file_name = os.path.basename(file_path)
        writer.write(file_name.encode() + b'\n')
        await writer.drain()

        with open(file_path, "rb") as file:
            while True:
                data = file.read(1024)
                if not data:
                    break
                writer.write(data)
                await writer.drain()
        print(f"File '{file_path}' inviato con successo al server.")
    except FileNotFoundError:
        print(f"File '{file_path}' non trovato.")

async def chat():
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 8888

    try:
        reader, writer = await asyncio.open_connection(SERVER_HOST, SERVER_PORT)

        file_path = input("Inserisci il percorso del file da inviare: ")
        await send_file(reader, writer, file_path)

    finally:
        print("Chiusura della connessione con il server...")
        writer.close()
        await writer.wait_closed()

asyncio.run(chat())



















