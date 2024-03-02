import asyncio

async def receive_message(reader):
    while True:
        data = await reader.readline()
        if not data:
            break
        print("Messaggio dal server:", data.decode().strip())

async def send_message(writer):
    while True:
        message = input("Inserisci il messaggio da inviare (scrivi 'exit' per uscire): ")
        writer.write(message.encode() + b'\n')
        await writer.drain()

        if message.lower() == 'exit':
            break

async def chat():
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 8888

    try:
        reader, writer = await asyncio.open_connection(SERVER_HOST, SERVER_PORT)

        # Avvio del task per ricevere i messaggi dal server
        asyncio.create_task(receive_message(reader))

        # Avvio del task per inviare i messaggi
        await send_message(writer)

    finally:
        print("Chiusura della connessione con il server...")
        writer.close()
        await writer.wait_closed()

asyncio.run(chat())


















