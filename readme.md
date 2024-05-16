subir:
ampy --port COM9 put main.py

formatear:
esptool.exe --chip esp32 --port COM9 erase_flash
esptool.exe --chip esp32 --port COM9 write_flash -z 0x1000 esp32-20240222-v1.22.2.bin




| GPIO | Entrada (Input) | Salida (Output)          | Notas                                                                                         |
|------|-----------------|--------------------------|-----------------------------------------------------------------------------------------------|
| 0    | Digital/Analógico (ADC2) | Digital                  | Salida PWM al inicio, debe estar LOW para modo flashing. Strapping pin. Touch (T1). ADC2: No usar con Wi-Fi. |
| 1    | Digital                  | Digital                  | Pin TX, salida de depuración al inicio.                                                       |
| 2    | Digital/Analógico (ADC2) | Digital                  | Conectado al LED interno, debe estar flotando o LOW para modo flashing. Touch (T2). Strapping pin. ADC2: No usar con Wi-Fi. |
| 3    | Digital                  | Digital                  | Pin RX, HIGH al inicio.                                                                       |
| 4    | Digital/Analógico (ADC2) | Digital                  | Touch (T0). Strapping pin. ADC2: No usar con Wi-Fi.                                           |
| 5    | Digital/Analógico (ADC2) | Digital                  | Salida PWM al inicio. Strapping pin. ADC2: No usar con Wi-Fi.                                 |
| 6    | No                       | No                       | Conectado a la memoria SPI flash integrada. No usar para otros propósitos.                    |
| 7    | No                       | No                       | Conectado a la memoria SPI flash integrada. No usar para otros propósitos.                    |
| 8    | No                       | No                       | Conectado a la memoria SPI flash integrada. No usar para otros propósitos.                    |
| 9    | No                       | No                       | Conectado a la memoria SPI flash integrada. No usar para otros propósitos.                    |
| 10   | No                       | No                       | Conectado a la memoria SPI flash integrada. No usar para otros propósitos.                    |
| 11   | No                       | No                       | Conectado a la memoria SPI flash integrada. No usar para otros propósitos.                    |
| 12   | Digital/Analógico (ADC2) | Digital                  | Falla en el arranque si está HIGH. Strapping pin. Touch (T5). ADC2: No usar con Wi-Fi.        |
| 13   | Digital/Analógico (ADC2) | Digital                  | Touch (T4). ADC2: No usar con Wi-Fi.                                                          |
| 14   | Digital/Analógico (ADC2) | Digital                  | Salida PWM al inicio. Touch (T6). Strapping pin. ADC2: No usar con Wi-Fi.                     |
| 15   | Digital/Analógico (ADC2) | Digital                  | Salida PWM al inicio. Strapping pin. Touch (T3). ADC2: No usar con Wi-Fi.                     |
| 16   | Digital                  | Digital                  | -                                                                                             |
| 17   | Digital                  | Digital                  | -                                                                                             |
| 18   | Digital                  | Digital                  | SPI_CLK.                                                                                      |
| 19   | Digital                  | Digital                  | SPI_MISO.                                                                                     |
| 21   | Digital                  | Digital                  | I2C_SDA.                                                                                      |
| 22   | Digital                  | Digital                  | I2C_SCL.                                                                                      |
| 23   | Digital                  | Digital                  | SPI_MOSI.                                                                                     |
| 25   | Digital/Analógico (ADC2) | Digital/Analógico (DAC)  | DAC1. ADC2: No usar con Wi-Fi.                                                                |
| 26   | Digital/Analógico (ADC2) | Digital/Analógico (DAC)  | DAC2. ADC2: No usar con Wi-Fi.                                                                |
| 27   | Digital/Analógico (ADC2) | Digital                  | Touch (T7). ADC2: No usar con Wi-Fi.                                                          |
| 32   | Digital/Analógico (ADC1) | Digital                  | Touch (T9).                                                                                   |
| 33   | Digital/Analógico (ADC1) | Digital                  | Touch (T8).                                                                                   |
| 34   | Digital/Analógico (ADC1) | No                       | Solo entrada.                                                                                 |
| 35   | Digital/Analógico (ADC1) | No                       | Solo entrada.                                                                                 |
| 36   | Digital/Analógico (ADC1) | No                       | Solo entrada.                                                                                 |
| 39   | Digital/Analógico (ADC1) | No                       | Solo entrada.                                                                                 |

### Notas Adicionales:

- **ADC1 vs. ADC2**: Los pines ADC2 no se pueden usar cuando se usa Wi-Fi.
- **Strapping Pins**: Pines GPIO0, GPIO2, GPIO4, GPIO5, GPIO12 y GPIO15 tienen funciones especiales en el arranque.
- **Pines de Entrada Digital Solo (GPI)**: GPIO34, GPIO35, GPIO36 y GPIO39 son solo de entrada.
- **Capacitive Touch**: GPIO0, GPIO2, GPIO4, GPIO12, GPIO13, GPIO14, GPIO15, GPIO27, GPIO32 y GPIO33 tienen sensores táctiles capacitivos.
- **Pines SPI Flash**: GPIO6, GPIO7, GPIO8, GPIO9, GPIO10 y GPIO11 están conectados a la memoria SPI flash y no se deben usar para otros propósitos.
