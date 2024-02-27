import paho.mqtt.client as mqtt
from random import randrange,uniform
import time
mqttBroker="mqtt.eclipseprojects.io"
client=mqtt.Client("Temperature_Inside")
client.connect(mqttBroker)
while True:
    randomNumber=uniform(20.0,22.0)
    client.publish("TEMPERATURE_OUTSIDE",randomNumber,1)
    print("Just Published: " + str(randomNumber) + " TEMPERATURE_OUTSIDE")
    time.sleep(1)
