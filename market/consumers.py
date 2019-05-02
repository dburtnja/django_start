import asyncio
from channels.consumer import AsyncConsumer


class TestConsumer(AsyncConsumer):

    def websocket_connect(self, event):
        print("event:", event)

