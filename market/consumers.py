import asyncio
from channels.consumer import AsyncConsumer
from time import sleep


class TestConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print("event:", event)
        await self.send({
            "type": "websocket.accept"
        })
        while True:
            await asyncio.sleep(5)
            await self.send({
                'type': 'websocket.send',
                'text': "test",
            })

    async def websocket_receive(self, event):
        print("received:", event)
