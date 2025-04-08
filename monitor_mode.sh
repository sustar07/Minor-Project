#!/bin/bash

# Check if wlan1 exists
if ! iwconfig wlan1 > /dev/null 2>&1; then
    echo "Error: wlan1 interface not found!"
    exit 1
fi

echo "[+] Setting wlan1 down..."
sudo ip link set wlan1 down

echo "[+] Enabling monitor mode..."
sudo iw dev wlan1 set type monitor

echo "[+] Setting wlan1 up..."
sudo ip link set wlan1 up

echo "[+] Verifying mode..."
iwconfig wlan1 | grep "Mode"

echo "[+] Done! wlan1 is now in monitor mode."

