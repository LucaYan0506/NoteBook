from cgitb import text
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatRoomConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' and self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )    

    async def receive(self, text_data):
        print(self.room_group_name)
        user = json.loads(text_data)['user']
        message = json.loads(text_data)['message']
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type' : 'send_message',
                'message' : message,
                'user' : user,
            }
        )    

    async def send_message(self,event):
        await self.send(text_data=json.dumps({
            'message' : event['message'],
            'user' : event['user'],
        }))