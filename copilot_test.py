import os

def print_system_uptime():
    try:
        # For Unix/Linux systems
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            uptime_hours = uptime_seconds / 3600
            print(f"System Uptime: {uptime_hours:.2f} hours")
    except FileNotFoundError:
        # For systems without /proc/uptime (e.g., Windows)
        if os.name == 'nt':
            import subprocess
            output = subprocess.check_output("net stats srv", shell=True).decode()
            for line in output.split('\n'):
                if "Statistics since" in line:
                    print(f"System Uptime: {line.strip()}")
        else:
            print("Could not determine system uptime.")

if __name__ == "__main__":
    print_system_uptime()
