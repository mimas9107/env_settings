#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import requests

def get_ip_outer():
    ip = requests.get('https://api.ipify.org').text
    return ip

def get_ip_internal():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def main():
    print("outer ip : ",get_ip_outer())
    print("internal ip : ",get_ip_internal())

if __name__ == "__main__":
    main()