#!/usr/bin/env bash
sudo apt install ufw -y
sudo ufw enable
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
