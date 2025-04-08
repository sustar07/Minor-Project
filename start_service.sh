#!/bin/bash

SERVICE_NAME="wramp_service"
LOG_FILE="/var/log/wramp.log"

echo "[+] Starting WRAMP background service..."
nohup python3 ramp.py > "$LOG_FILE" 2>&1 &
echo $! > /tmp/$SERVICE_NAME.pid

echo "[+] WRAMP service started with PID $(cat /tmp/$SERVICE_NAME.pid)"

