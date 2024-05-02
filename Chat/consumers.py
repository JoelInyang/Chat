import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Am broadcasting the message to all connected clients
        self.channel_layer.group_send(
            'chat_room',  # The group name 
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def chat_message(self, event):
        # Am sending the received message to the client
        message = event['message']
        self.send(text_data=json.dumps({
            'message': message
        }))



from firebase_admin import messaging

def send_push_notification(token, message_body):
    message = messaging.Message(
        data={
            'message': message_body
        },
        token=token,
    )
    response = messaging.send(message)
    print('Successfully sent message:', response)



from firebase_admin import messaging

def subscribe_to_topic(token, topic_name):
    response = messaging.subscribe_to_topic(token, topic_name)
    print('Successfully subscribed:', response)
