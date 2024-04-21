import subprocess

def create_fake_wifi(ssid, interface):
    command = f"airbase-ng -e '{ssid}' -c 6 {interface}"
    subprocess.Popen(command, shell=True)

def main():
    ssid = "FakeWiFi"
    interface = "wlan0"  # Replace with your wireless interface
    create_fake_wifi(ssid, interface)

if __name__ == "__main__":
    main()
