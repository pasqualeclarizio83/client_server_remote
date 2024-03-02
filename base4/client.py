import asyncio

async def send_message():
    # Indirizzo IP e porta del server
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 8888

    # Connessione al server
    reader, writer = await asyncio.open_connection(SERVER_HOST, SERVER_PORT)

    try:
        while True:
            # Input del messaggio dall'utente
            message = input("Inserisci il messaggio da inviare al server (scrivi 'exit' per uscire): ")

            # Invio del messaggio al server
            writer.write(message.encode() + b'\n')
            await writer.drain()

            if message.lower() == 'exit':
                break

    finally:
        # Chiusura della connessione
        print("Chiusura della connessione con il server...")
        writer.close()
        await writer.wait_closed()

asyncio.run(send_message())



