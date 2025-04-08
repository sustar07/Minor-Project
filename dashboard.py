import subprocess
import time
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.prompt import Prompt

console = Console()

def send_sms(phone_number, message):
    console.print("[bold yellow]Unlocking phone...[/bold yellow]")
    subprocess.run(["bash", "unlock.sh"])
    time.sleep(10)
    console.print(f"[bold green]Sending SMS to {phone_number}...[/bold green]")
    cmd = f'adb shell service call isms 5 i32 0 s16 "com.android.mms.service" s16 "{phone_number}" s16 "null" s16 "{message}" s16 "null" s16 "null"'
    subprocess.run(cmd, shell=True)
    console.print("[bold cyan]Message sent![/bold cyan]")

def check_ssh_status():
    result = subprocess.run("pgrep ssh", shell=True, stdout=subprocess.PIPE)
    return "[green]Running[/green]" if result.stdout else "[red]Stopped[/red]"

def read_latest_sms(phone_number):
    cmd = f'adb shell content query --uri content://sms/inbox --where "address=\'{phone_number}\'" --sort "date DESC" --limit 1'
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, text=True)
    return result.stdout.strip() or "[red]No messages found.[/red]"

def show_dashboard():
    table = Table(title="📡 WRAMP CLI Dashboard")
    table.add_column("Option", justify="center", style="bold cyan")
    table.add_column("Description", justify="left")

    table.add_row("[1]", "Start Background Service")
    table.add_row("[2]", "Stop Background Service")
    table.add_row("[3]", "Unlock Phone & Send SMS")
    table.add_row("[4]", "Check SSH Status")
    table.add_row("[5]", "Read Latest SMS")
    table.add_row("[Q]", "[bold red]Quit[/bold red]")

    return table

def main():
    while True:
        console.clear()
        console.print(show_dashboard())
        console.print(f"\n[bold yellow]SSH Status:[/bold yellow] {check_ssh_status()}")

        choice = Prompt.ask("\n[bold green]Choose an option[/bold green]")

        if choice == "1":
            console.print("[bold cyan]Starting background service...[/bold cyan]")
            subprocess.run(["bash", "start_service.sh"])
        elif choice == "2":
            console.print("[bold red]Stopping background service...[/bold red]")
            subprocess.run(["bash", "stop_service.sh"])
        elif choice == "3":
            phone_number = Prompt.ask("[bold magenta]Enter phone number[/bold magenta]")
            message = Prompt.ask("[bold magenta]Enter message[/bold magenta]")
            send_sms(phone_number, message)
        elif choice == "4":
            console.print(f"[bold yellow]SSH Status:[/bold yellow] {check_ssh_status()}")
        elif choice == "5":
            phone_number = Prompt.ask("[bold blue]Enter phone number to read SMS[/bold blue]")
            sms = read_latest_sms(phone_number)
            console.print(f"[bold cyan]Latest SMS:[/bold cyan] {sms}")
        elif choice.lower() == "q":
            console.print("[bold red]Exiting...[/bold red]")
            break
        else:
            console.print("[bold red]Invalid option! Try again.[/bold red]")

        time.sleep(2)

if __name__ == "__main__":
    main()

