# Copy by Flavio Lages

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
    [x]i2c2
or 
edit /boot/armbianEnv.txt file with “nano /boot/armbianEnv.txt“
add “overlays=i2c0 i2c1 i2c2“
# nano /etc/modules 
or 
$ sudo nano /etc/modules 
    i2c-dev
    i2c-bcm2708

# reboot 
or 
$ sudo reboot
Check i2c enable 

i2cdetect -y 0
i2cdetect -y 1


[Requiriments]
# apt install i2c-tools libi2c-dev python3-smbus 
or
$ sudo apt install i2c-tools libi2c-dev python3-smbus

Install :

cd home/

git clone https://github.com/dnmnhat/lcd16x2.git

cd lcd16x2/

python3 time_date.py

Crontab

sudo crontab -e

@reboot sleep 10 && /home/lcd16x2/time_date.py


And Reboot.
