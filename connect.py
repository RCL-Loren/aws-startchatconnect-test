import boto3
import json
import asyncio
import websockets
import ssl

client = boto3.client('connect')

#required
# InstanceId
# ContactFlowId
# ParticipantDetails

#optional

response = client.start_chat_contact(
    InstanceId='97f8364a-b438-489e-bc27-241e3210f694',
    ContactFlowId='0ecd1ecd-734a-4250-9b1c-c07409438adc',
    Attributes={
        'string': 'string'
    },
    ParticipantDetails={
        'DisplayName': 'Test User'
    },
    InitialMessage={
        'ContentType': 'text/plain',
        'Content': 'Hi there'
    },
)

ptoken = response['ParticipantToken'] 

print(ptoken)

participant_client = boto3.client('connectparticipant')

response = participant_client.create_participant_connection(
    Type=['WEBSOCKET',
    ],
    ParticipantToken=ptoken
)

print(response) 


#Websocket': {'ConnectionExpiry': '2019-11-25T00:18:36.674Z', 'Url': 

mysocket = print(response['Websocket']['Url'])

async def hello():
    uri = mysocket
    async with websockets.connect(
        uri, ssl=true
    ) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())

