import I2C_LCD_driver
import time 

#Init driver
lcd = I2C_LCD_driver.lcd()

while True:
    localtime = time.localtime()
    hora = time.strftime("%I:%M:%S %p", localtime)
    lcd.lcd_display_string(hora, 1)
    time.sleep(1)
    mylcd.lcd_clear()


#import time
#while True:
#  localtime = time.localtime()
#  result = time.strftime("%I:%M:%S %p", localtime)
#  print(result, end="", flush=True)
#  print("\r", end="", flush=True)
#  time.sleep(1)

