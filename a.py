import os

def scan_wifi():
    try:
        # Execute the nmcli command to list available wireless networks
        result = os.popen('nmcli device wifi list').read()

        # Extract SSID and signal strength information from the result
        networks = []
        lines = result.split('\n')[1:]  # Skip header line
        for line in lines:
            if line.strip():
                fields = line.split()
                ssid = fields[0]
                signal_strength = fields[7]
                networks.append({'SSID': ssid, 'Signal Strength': signal_strength})

        if not networks:
            print("No wireless networks found.")
        else:
            print("Available wireless networks:")
            for network in networks:
                print(f"SSID: {network['SSID']}, Signal Strength: {network['Signal Strength']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    scan_wifi()
