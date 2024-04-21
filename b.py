import subprocess

def create_wifi_network(ssid, password):
    command = f"termux-wifi-hotspot create {ssid} {password}"
    subprocess.run(command, shell=True)

def main():
    create_wifi_network('haha', 'haha')
    create_wifi_network('ad', 'ad')

if __name__ == "__main__":
    main()
