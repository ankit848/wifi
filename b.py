import subprocess

def create_wifi_network(ssid, password):
    # Configure hostapd
    hostapd_conf = f"""interface=wlan0
ssid={ssid}
hw_mode=g
channel=7
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase={password}
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP"""
    with open('/etc/hostapd/hostapd.conf', 'w') as f:
        f.write(hostapd_conf)

    # Configure dnsmasq
    dnsmasq_conf = f"""interface=wlan0
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h"""
    with open('/etc/dnsmasq.conf', 'w') as f:
        f.write(dnsmasq_conf)

    # Start hostapd and dnsmasq
    subprocess.run(['systemctl', 'start', 'hostapd'])
    subprocess.run(['systemctl', 'start', 'dnsmasq'])

if __name__ == "__main__":
    ssid1 = "MyNetwork1"
    password1 = "password1"
    ssid2 = "MyNetwork2"
    password2 = "password2"

    create_wifi_network(ssid1, password1)
    create_wifi_network(ssid2, password2)
