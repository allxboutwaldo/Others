#pip install speedtest-cli

import speedtest 
import os
from colorama import init, Fore, Style

init()

os.system('cls' if os.name == 'nt' else 'clear')

# AERON ASCII ART
waldo_art = r"""
 █████╗ ███████╗██████╗ ██████╗ ███╗   ██╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗  ██║
███████║█████╗  ██████╔╝██║  ██║██╔██╗ ██║
██╔══██║██╔══╝  ██╔══██╗██║  ██║██║╚██╗██║
██║  ██║███████╗██║  ██║╚█████╔╝██║ ╚████║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
         INTERNET TESTING SPEED
"""
print(Fore.CYAN + Style.BRIGHT + waldo_art),

def check_internet_speed():
    st = speedtest.Speedtest()

    print(Fore.WHITE + "🚀 Testing speed....")

    download = st.download() / 1_000_000
    upload = st.upload() / 1_000_000

    st.get_best_server()
    ping = st.results.ping

    return {
        "download": round(download, 2),
        "upload": round(upload, 2),
        "ping": round(ping, 2)
    }

speed = check_internet_speed()

print(Fore.WHITE + f"⬇️ Download: {speed['download']} Mbps"),
print(Fore.WHITE + f"⬆️ Upload: {speed['upload']} Mbps"),
print(Fore.WHITE + f"🕛 Ping: {speed['ping']} ms"),

# Keep the CMD window open
input("Press Enter to exit...")
