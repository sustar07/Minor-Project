#!/bin/bash
sleep 10  # Wait for PPP to start
ip route add default via 192.168.1.1 dev wlan0

