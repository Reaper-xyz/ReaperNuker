# For spamming webhooks
import requests
import time


def sendmessage(webhook, message):
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(webhook, json={"content": message}, headers = headers)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        return False
    
def spamwebhook(webhookin, messagein , ammount):
    max = 0
    while max < ammount :
        max =+ 1
        sendmessage(webhookin, messagein)


