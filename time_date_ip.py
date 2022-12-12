import I2C_LCD_driver
import time
from time import sleep
from datetime import datetime
from subprocess import check_output
mylcd = I2C_LCD_driver.lcd()
IP = check_output(["hostname", "-I"]).split()[0]
IP = IP.decode('ascii')
def get_mem_info():
    men_info = []
    info = subprocess.getoutput('free -m|grep Mem:').split(' ')
    for i in info:
        if i != '':
            men_info.append(i)
        else:
            continue
    men_info_str='Mem: '+men_info[3] + 'M/' + men_info[1] + 'M'
    return men_info_str


while True:
 #mylcd.lcd_display_string( datetime.now().strftime('%b %d  %H:%M:%S\n'), 2)
 
 mylcd.lcd_display_string("IP: %s" %str(IP), 1)
 
 mylcd.lcd_display_string('%Mem ' + get_mem_usage_rate()2)
