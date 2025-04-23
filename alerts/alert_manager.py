import requests

def send_alert(message, webhook_url):
    payload = {"text": message}
    requests.post(webhook_url, json=payload)
