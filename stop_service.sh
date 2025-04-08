#!/bin/bash

SERVICE_NAME="wramp_service"

if [ -f "/tmp/$SERVICE_NAME.pid" ]; then
    PID=$(cat /tmp/$SERVICE_NAME.pid)
    echo "[+] Stopping WRAMP service (PID: $PID)..."
    kill "$PID" && rm -f "/tmp/$SERVICE_NAME.pid"
    echo "[+] WRAMP service stopped."
else
    echo "[!] No running WRAMP service found."
fi

