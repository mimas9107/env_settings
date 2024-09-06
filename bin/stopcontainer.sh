#!/usr/bin/env bash
echo -e '======== Stoping docker/containerd ========'
sudo systemctl stop docker.socket
sudo systemctl stop containerd
