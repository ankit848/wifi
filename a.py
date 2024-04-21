import subprocess

def scan_wifi():
    try:
        # Execute the iwlist command to scan for available networks
        result = subprocess.check_output(['iwlist', 'wlan0', 'scan'])
        result = result.decode('utf-8')

        # Extract SSID and signal strength information from the result
        networks = []
        lines = result.split('\n')
        ssid = None
        for line in lines:
            if 'ESSID' in line:
                ssid = line.split('"')[1]
            elif 'Signal level' in line:
                if ssid:
                    signal_strength = line.split('=')[-1].split('/')[0]
                    networks.append({'SSID': ssid, 'Signal Strength': signal_strength})
                    ssid = None

        if not networks:
            print("No wireless networks found.")
        else:
            print("Available wireless networks:")
            for network in networks:
                print(f"SSID: {network['SSID']}, Signal Strength: {network['Signal Strength']}")
    except subprocess.CalledProcessError:
        print("Error: Failed to scan for wireless networks.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    scan_wifi()
