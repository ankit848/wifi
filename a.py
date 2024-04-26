import subprocess
import re

def monitor_wifi(interface):
    try:
        # Run tcpdump to capture WiFi traffic
        process = subprocess.Popen(['tcpdump', '-i', interface, 'subtype', 'probe-req'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        print("Monitoring WiFi for connection attempts...")

        # Parse captured packets
        for line in iter(process.stdout.readline, ''):
            # Extract SSID from probe request
            match = re.search(r'SSID: "(.*)"', line)
            if match:
                ssid = match.group(1)

                # Extract password from captured packets
                match = re.search(r'password=(\w+)', line)
                if match:
                    password = match.group(1)
                    print(f"SSID: {ssid}, Password: {password}")

    except KeyboardInterrupt:
        print("\nExiting...")

def main():
    wifi_interface = "wlan0"  # Replace with your WiFi interface name
    monitor_wifi(wifi_interface)

if __name__ == "__main__":
    main()
