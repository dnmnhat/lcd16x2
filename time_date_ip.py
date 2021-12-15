import I2C_LCD_driver
import time
from time import sleep
from datetime import datetime
from subprocess import check_output
mylcd = I2C_LCD_driver.lcd()
IP = check_output(["hostname", "-I"]).split()[0]
IP = IP.decode('ascii')



while True:
 mylcd.lcd_display_string(%time.strftime("%b %d %H:%M:%S"), 2)
 
 mylcd.lcd_display_string("IP: %s" %str(IP), 1)
