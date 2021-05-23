import I2C_LCD_driver
from time import 

while True:
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    mylcd.lcd_display_string(result, 1)
    time.sleep(1)
    mylcd.lcd_clear()


#import time
#while True:
#  localtime = time.localtime()
#  result = time.strftime("%I:%M:%S %p", localtime)
#  print(result, end="", flush=True)
#  print("\r", end="", flush=True)
#  time.sleep(1)

