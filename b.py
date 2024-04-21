import os

def create_wifi_network(ssid, password):
    # Set up the wireless interface as an access point
    os.system("ip link set wlan0 down")
    os.system("ip addr flush dev wlan0")
    os.system("ip link set wlan0 up")
    os.system(f"iw wlan0 set type managed")
    os.system(f"iw wlan0 ibss join {ssid} {password} 2432")

    # Configure DHCP server using dnsmasq
    with open('/data/data/com.termux/files/etc/dnsmasq.conf', 'w') as f:
        f.write(f"interface=wlan0\n")
        f.write(f"dhcp-range=192.168.43.10,192.168.43.100,255.255.255.0,24h\n")

    # Start dnsmasq
    os.system("dnsmasq -C /data/data/com.termux/files/etc/dnsmasq.conf")

def main():
    create_wifi_network('haha', 'haha')
    create_wifi_network('ad', 'ad')

if __name__ == "__main__":
    main()
