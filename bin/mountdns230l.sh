#!/bin/bash
mount -t cifs -o username=mimas,vers=1.0,iocharset=utf8,file_mode=0777,dir_mode=0777,soft,user,noperm //192.168.1.33/MP3_1 /mnt/smb/hd1
mount -t cifs -o username=mimas,vers=1.0,iocharset=utf8,file_mode=0777,dir_mode=0777,soft,user,noperm //192.168.1.33/MP3_2 /mnt/smb/hd2
