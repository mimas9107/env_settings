#!/bin/bash
echo -e ' ======= Stop the SAMBA service ====== '
sudo systemctl stop smbd
sudo systemctl stop smb*
sudo systemctl stop nmbd
sudo systemctl stop winbind*
