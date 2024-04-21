import wifi

def scan_wifi():
    # Scan for available wireless networks
    networks = wifi.Cell.all('wlan0')

    if not networks:
        print("No wireless networks found.")
    else:
        print("Available wireless networks:")
        for network in networks:
            print(f"SSID: {network.ssid}, Signal Strength: {network.signal}")
            
if __name__ == "__main__":
    scan_wifi()
