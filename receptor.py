import network
import espnow
import ujson as json
import binascii
from machine import Pin, PWM, ADC
import time


# Configurar ESP-NOW
sta = network.WLAN(network.STA_IF)
sta.active(True)
e = espnow.ESPNow()
e.active(True)
mac = "e0:5a:1b:a6:cb:f8"

peer = binascii.unhexlify(mac.replace(':', ''))
e.add_peer(peer)
print(f"Peer agregado: {peer}")

#set servo
servo_pin = 13  # PWM pin for servo control
servo_pwm = PWM(Pin(servo_pin), freq=50)

joystick_min = 0
joystick_max = 4095
servo_min = 40
servo_max = 115


def map_value(value, in_min, in_max, out_min, out_max):
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


# Función para recibir el nivel de batería de la segunda ESP32
def recibir_json(data):
    dict_data = json.loads(data)
    return dict_data

# Bucle principal
def main_loop():
    while True:
        host, msg = e.recv()
        if msg:
            data = recibir_json(msg)
            print(data)
            servo_angle = map_value(int(data["servo1"]), joystick_min, joystick_max, servo_min, servo_max)
            servo_pwm.duty(servo_angle)
        
            #print(host, msg)
        
