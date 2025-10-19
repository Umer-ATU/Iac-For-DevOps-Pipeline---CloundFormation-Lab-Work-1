import json
import boto3
import os
import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    method = event.get('httpMethod')
    path = event.get('path', '')

    if method == "POST" and path.endswith("/note"):
        body = json.loads(event['body'])
        topic = body.get('topic')
        note = body.get('note')
        date = datetime.datetime.utcnow().isoformat()

        if not topic or not note:
            return response(400, {'error': 'topic and note required'})

        table.put_item(Item={'topic': topic, 'note': note, 'date': date})
        return response(201, {'message': 'Note added successfully', 'topic': topic})

    elif method == "GET" and '/note/' in path:
        topic = event.get('pathParameters', {}).get('topic')
        if not topic:
            return response(400, {'error': 'topic parameter missing'})

        res = table.get_item(Key={'topic': topic})
        if 'Item' in res:
            return response(200, res['Item'])
        else:
            return response(404, {'error': 'Note not found'})

    return response(405, {'error': 'Unsupported method'})

def response(status, body):
    return {
        'statusCode': status,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(body)
    }
