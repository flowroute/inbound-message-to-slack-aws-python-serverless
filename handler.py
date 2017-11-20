from botocore.vendored import requests
import json

#Paste your Slack webhook URL below 
webhook_url = '<your-Slack-webhook-url>'

def message_to_slack(event, context):
    parsed = json.loads(event['body'])
    response = requests.post(
        webhook_url,
        json={'text': json.dumps(parsed, indent=4, sort_keys=True,
   ensure_ascii=False)}
    )

    http_reply = {
        "statusCode": 200,
        "body": response.text
    }

    return http_reply
