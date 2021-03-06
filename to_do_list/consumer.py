from channels.generic.websocket import AsyncWebsocketConsumer
import json

class NoteRoomConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'note_%s' and self.room_name

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
        message = json.loads(text_data)['message']
        user = json.loads(text_data)['user']
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type' : 'update',
                'message' : message,
                'user' : user,
            }
        )    

    async def update(self,event):
        await self.send(text_data=json.dumps({
            'message' : event['message'],
            'user' : event['user'],
        }))