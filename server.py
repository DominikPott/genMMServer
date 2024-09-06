import asyncio
import json
import websockets


async def handle_client(websocket, path):
    try:
        # Empfange die Nachricht des Clients
        message = await websocket.recv()
        data = json.loads(message)
        print(f"Empfangene Daten vom Client: {data}")

        # Beantworte die Anfrage mit einer JSON-Nachricht
        response = {"status": "success", "received_data": data}
        await websocket.send(json.dumps(response))
    except websockets.ConnectionClosed:
        print("Verbindung geschlossen")


async def main():
    server = await websockets.serve(handle_client, "localhost", 7765)
    await server.wait_closed()


asyncio.run(main())
