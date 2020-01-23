import random
import time

from pythonosc import udp_client

def send(ip,port,message):
    client = udp_client.SimpleUDPClient(ip, port)
    client.send_message("/wek/inputs",message)


if __name__ == "__main__":

  for x in range(10):
    send("127.0.0.1",5005,x)
    time.sleep(1)
