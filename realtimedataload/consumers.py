from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.layers import get_channel_layer
import json
from .lib.covid19 import GetCovid19RealtimeData

class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        data = GetCovid19RealtimeData()
        self.room_name = str(self.channel_name.split("!")[1])
        await(self.channel_layer.group_add)(
            self.room_name,self.channel_name
        )

        await self.send(text_data=json.dumps({"msg":"Wellcome"}))

        await(self.channel_layer.group_send)(
            self.room_name,{
                "type":"get_all_data",
                "message":data
            }
        )
    async def get_all_data(self,event): 
        message = event["message"]
        await self.send(text_data=json.dumps(message))

    async def receive(self, text_data=None, bytes_data=None):
        print("From receiver --> ",text_data)
        await self.send(text_data=text_data)

    async def disconnect(self):
        await self.close()