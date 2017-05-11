import boto3
import json

print("start simple function")

client = boto3.client('lambda')


def handle(event, context):

    response = client.invoke(
        FunctionName='apex_prototype_namer',
        InvocationType='Event',
        Payload=json.dumps(event)
    )

    print(response)

    #return json.dumps(response)
