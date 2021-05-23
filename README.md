# by Flavio Lages
LCD 16x2 i2c - Orangepi Lite

# Comands mode superuser (root)
$ Comands mode usuer (sudo)

[enable module i2c]
# armbian-config 
or 
$ sudo armbian-config 
    HHardware - toggle board low level functions: UART, I2C, SPI, …
    [x]i2c
    [x]i2c1

# vi /etc/modules 
or 
$ sudo /etc/modules 
    i2c-dev
    i2c-bcm2708

# reboot 
or 
$ sudo reoobt


[Requiriments]
# apt install i2c-tools libi2c-dev python-smbus 
or
$ sudo apt install i2c-tools libi2c-dev python-smbus
