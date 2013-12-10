SGDialer
========

Stargate dialing simulator written in Python designed to run on Raspberry Pi.


Hardware Setup
==============

Setting up Wifi on Raspberry Pi with Edimax EW-7811Un USB dongle
----------------------------------------------------------------

1.  `sudo nano /etc/network/interfaces`
2.  Add the following:

    ```
    auto wlan0
    iface wlan0 inet dhcp
    wireless-essid myessid #router ssid
    wireless-mode managed

    wpa-ssid myessid #router ssid
    wpa-psk my-encryption-key #router password
    ```

3.  For a static IP, change/add the following:

    ```
    address 192.168.1.6 #desired IP address of Pi
    netmask 255.255.255.0
    network 192.168.1.0 #low IP range of network
    broadcast 192.168.1.255 #high IP range of network
    gateway 192.168.1.1 #IP address of router
    ```

4.  Edit the config file to control dongle power settings: `sudo nano /etc/modprobe.d/8192cu.conf`

5.  Add the following to disable power management:
    `options 8192cu rtw_power_mgnt=0 rtw_enusbss=0`

6.  Edit the crontab: `sudo crontab -e`

7.  Add the following to set the Pi to ping the router every 500ms:

    `*/1 * * * * ping -c 1 192.168.1.1 #replace IP address with that of your router`

8.  Connect to internet via wired network.

9.  Run `sudo apt-get update`

10. Run `sudo apt-get install wpasupplicant`

11. Reboot the Pi