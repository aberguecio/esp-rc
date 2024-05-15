subir:
ampy -d 0.5 --port COM5 put "...\main.py"

formatear:
esptool.py --chip esp32 --port COM5 erase_flash
esptool.py --chip esp32 --port COM4 write_flash -z 0x1000 "C:\Users\...\esp32-20230426-v1.20.0.bin"