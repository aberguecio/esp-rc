import network
import espnow
import ujson as json
import binascii
import time
import machine
from machine import Pin, PWM, ADC

# Configurar ESP-NOW
sta = network.WLAN(network.STA_IF)
sta.active(True)
e = espnow.ESPNow()
e.active(True)

mac = "e8:31:cd:d6:ef:d4"
peer = binascii.unhexlify(mac.replace(':', ''))
e.add_peer(peer)
print(f"Peer agregado: {peer}")

#setup joystick
joystick_x_pin = 34  # ADC pin for joystick X-axis
joystick_x = ADC(Pin(joystick_x_pin))
joystick_min = -4095
joystick_max = 4095

# Función para enviar el nivel de batería a la primera ESP32
def enviar_json(data):
    mensaje = {
        "numero": data[0],
        "servo1": data[1],
    }
    mensaje = json.dumps(mensaje)
    print(f"Mensaje enviado: {mensaje}")
    e.send(json.dumps(mensaje))

# Bucle principal
def main_loop():
    i=0
    while True:
        # Enviar el nivel de batería a la primera ESP32
        x_value = joystick_x.read()
        enviar_json([i,x_value])
        i=i+1