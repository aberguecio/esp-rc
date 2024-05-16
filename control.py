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

mac = "d4:d4:da:e4:b7:c8"
peer = binascii.unhexlify(mac.replace(':', ''))
e.add_peer(peer)
print(f"Peer agregado: {peer}")

#setup joystick

joystick_x = ADC(Pin(33))
joystick_x.atten(ADC.ATTN_11DB)
joystick_y = ADC(Pin(32))
joystick_y.atten(ADC.ATTN_11DB)


def enviar_json(data):
    mensaje = {
        "servo_0": data[0],
        "servo1": data[1],
    }
    mensaje = json.dumps(mensaje)
    print(f"Mensaje enviado: {mensaje}")
    try:
        e.send(peer, mensaje)
    except OSError as ex:
        print(f"Error al enviar mensaje: {ex}")


# Bucle principal
def main_loop():
    while True:
        y_value = joystick_y.read()
        x_value = joystick_x.read()
        enviar_json([y_value,x_value])
        time.sleep(0.01)
