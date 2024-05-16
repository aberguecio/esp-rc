program_name = "receptor" # "control", "receptor", "mac"
import machine
import time

def led_blink(times=0, delay=0.3):
    led = machine.Pin(2, machine.Pin.OUT)
    if times == 0:
        while True:
            led.value(not led.value())
            time.sleep(delay)
    else:
        for _ in range(times*2):
            led.value(not led.value())
            time.sleep(delay)

try:
    if program_name == "control":
        import control
        led_blink(1)
        control.main_loop()
    elif program_name == "receptor":
        import receptor
        led_blink(2)
        receptor.main_loop()
    elif program_name == "mac":
        import mac
        led_blink(3)
        mac
except Exception as e:
    print("An error occurred:", str(e))
    led_blink(100, 0.1)