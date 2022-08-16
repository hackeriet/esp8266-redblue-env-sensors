import network
import time
import machine
import ujson
import ubinascii
import sys

from umqtt.simple import MQTTClient
from machine import ADC

CLIENT_ID = ubinascii.hexlify(machine.unique_id())

with open('config.json') as fp:
    config = ujson.loads(fp.read())

print("Connecting to wifi: " + config['wifi']['ssid'])

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(config['wifi']['ssid'],config['wifi']['psk'])

while not station.isconnected():
    machine.idle()

print("Connected: " + str(station.ifconfig()))

# Disabling the access point
ap_if = network.WLAN(network.AP_IF)
if ap_if.active(): ap_if.active(False)

def name():
    return config['name'];

def mqtt():
    c = MQTTClient(client_id = CLIENT_ID,
               server     = config['mqtt']['server'],
               user       = config['mqtt']['user'],
               password   = config['mqtt']['password'],
               port       = config['mqtt']['port'],
               ssl        = config['mqtt']['ssl']
    )
    c.connect()
    return c

def mqtt_publish(c, k, v):
    topic_prefix = config['mqtt']['topic_prefix']
    c.publish(topic_prefix + k, str(v), True)




