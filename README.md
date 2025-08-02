# WRAMP - Wireless Remote Attack and Monitoring Platform

WRAMP (Wireless Remote Attack and Monitoring Platform) is a portable, low-power, remotely accessible cyberattack and surveillance toolkit designed for red teaming, penetration testing, and field monitoring. It integrates wireless network scanning, attack execution, remote shell access, and update capabilities into a compact hardware setup built on the Raspberry Pi Zero 2 W.

## 🧠 Project Summary

WRAMP is a **proof-of-concept offensive security device** capable of:

- Scanning and identifying wireless devices in range
- Monitoring and logging traffic and OS fingerprints
- Executing modular wireless attacks
- Triggering XSS payloads via captive portal redirection
- Accessing a live shell remotely via LTE
- Self-updating and loading new payloads remotely

All this is done using **Python scripts**, **Linux networking tools**, and **lightweight hardware**, making WRAMP suitable for discreet field deployments and offensive cyber-experiments.

---

## ⚙️ System Architecture

### 🧩 Hardware Components

- **Raspberry Pi Zero 2 W**
- **External USB Wi-Fi Adapter (Monitor Mode + Packet Injection capable)**
- **Android Phone (for LTE tethering via USB-ECM or RNDIS)**
- **Battery Pack or Power Bank**

### 🧰 Software Stack

- **OS:** Raspberry Pi OS Lite (headless)
- **Language:** Python (main control interface)
- **Networking Tools:** `airmon-ng`, `airodump-ng`, `hostapd`, `dnsmasq`, `nmap`, `iptables`
- **Remote Access:** SSH (with LTE failover)


---

## 🚀 Features

| Feature                  | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| 📡 Network Scanner       | Uses airmon-ng and airodump-ng to scan nearby wireless networks             |
| 🔍 Device Profiler       | Captures MAC addresses, signal strength, and vendor IDs                     |
| 🧠 OS Fingerprinting     | Identifies probable OS types based on network fingerprinting                |
| 🎯 Modular Attacks       | Payload system to upload and trigger attack modules remotely                |
| 🌐 Remote Shell          | SSH access even over LTE (via USB-tethered Android)                         |       

---


https://docs.google.com/document/d/1IGIiYjft2drntA9s0fxmH5kirfHvUt3wZl1kePcrhWQ/edit?usp=sharing
