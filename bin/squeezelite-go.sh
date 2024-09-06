#!/usr/bin/bash
SQUEEZELITE=/usr/bin/squeezelite
LMSSERVER=192.168.1.112
OUTPUTDEVICE=default
MODELNAME=squeezelite-mimas
NAME=squeezelite-mimas

$SQUEEZELITE -s $LMSSERVER \
	-o $OUTPUTDEVICE \
	-M $MODELNAME \
	-n $NAME \
	-a 32 \
	-b 8192:19200 \
	-r 384000:5000 \
	-D 8192
