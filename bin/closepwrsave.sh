#!/usr/bin/env bash
#Some suggested solutions are:

#    Turn off bluetooth (use rfkill or turn off in Bios)
#    Turn OFF 802.11n mode (in /etc/modprobe.d/iwlwifi.conf add options iwlwifi 11n_disable=1)
#    Turn ON link aggregation (in /etc/modprobe.d/iwlwifi.conf add options iwlwifi 11n_disable=8)
#    Turn OFF watchdog (in /etc/modprobe.d/iwlwifi.conf add options iwlwifi wd_disable=1)
#    Turn off power saving features ($ sudo iw wlan0 set power_save off)
#    Set regulatory domain ($ sudo iw reg set <country code>)




sudo iw wlp3s0 set power_save off
