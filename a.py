import subprocess

def create_wifi_hotspot(ssid, password):
    try:
        # Enable the WiFi interface
        subprocess.run(['ip', 'link', 'set', 'wlan0', 'up'], check=True)
        
        # Set the IP address for the WiFi interface
        subprocess.run(['ip', 'addr', 'add', '192.168.43.1/24', 'dev', 'wlan0'], check=True)
        
        # Create the WiFi hotspot
        subprocess.run(['iw', 'dev', 'wlan0', 'ibss', 'join', ssid, '2412', 'key', 'd:0:' + password], check=True)

        print(f"WiFi hotspot '{ssid}' created with password '{password}'")
    except subprocess.CalledProcessError as e:
        print(f"Failed to create WiFi hotspot: {e}")

def main():
    ssid = "wifi"
    password = "pass"

    create_wifi_hotspot(ssid, password)

if __name__ == "__main__":
    main()
