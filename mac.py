from network import WLAN
import ubinascii
mac = ubinascii.hexlify(WLAN().config('mac'),':').decode()

print("MAC:",mac)