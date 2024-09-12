import docker
import datetime
import requests

client = docker.DockerClient(base_url='unix://var/run/docker.sock')

webhook_url = "SUA_URL" ##Webhook discord

for event in client.events(decode=True, filters={"event": "die"}):
    container_id = event["id"]
    container_name = event["Actor"]["Attributes"]["name"]
    epoch_time = event["time"]
    
    date = datetime.datetime.fromtimestamp(epoch_time)

    payload = {"content": "O container %s (%s) foi finalizado ás %s" % (container_name, container_id, date)} ## DICT discord

    print (payload) 
    requests.post(webhook_url, data=payload)