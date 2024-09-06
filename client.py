import asyncio
import json
import websockets


async def send_json_and_receive_response(uri, json_data):
    async with websockets.connect(uri) as websocket:
        # Sende die JSON-Daten an den Server
        await websocket.send(json.dumps(json_data))
        print(f"Gesendete Daten: {json_data}")

        # Warte auf eine Antwort vom Server
        response = await websocket.recv()

        # Konvertiere die Antwort in ein Python-Dictionary
        response_data = json.loads(response)
        print(f"Empfangene Antwort: {response_data}")

        return response_data


async def main():
    uri = "ws://localhost:7765"  # Die WebSocket-URL des Servers
    json_data = {"message": "Hallo Server!", "data": {"key": "value"}}

    response = await send_json_and_receive_response(uri, json_data)
    print(f"Server-Antwort: {response}")


asyncio.run(main())
