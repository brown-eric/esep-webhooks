import os
import json
import requests

def lambda_handler(event, context):
    body = event.get('body')
    if body:
        body = json.loads(body)
    else:
        return {"statusCode": 400, "body": "No body in event."}
    
    issue_url = body.get('issue', {}).get('html_url')
    issue_title = body.get('issue', {}).get('title')
    slack_webhook = os.environ['SLACK_WEBHOOK_URL']

    if not issue_url:
        return {"statusCode": 400, "body": "Invalid payload: no issue URL"}
    
    message = {"text": f"New GitHub Issue Created: {issue_title} - {issue_url}"}
    response = requests.post(slack_webhook, json=message)
    return {"statusCode": response.status_code, "body": "Slack notification sent."}
