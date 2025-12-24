import psutil
import time
import os



def check_ping():
    res = os.system("ping -c 1 8.8.8.8 > /dev/null 2>&1")
    return "online" if res == 0 else "offline"

def get_network_usage():
    net_io = psutil.net_io_counters()
    sent = net_io.bytes_sent / (1024 * 1024)
    recv = net_io.bytes_recv / (1024 * 1024)
    return  {"sent":sent,"recv":recv}
def display():
    print("--- Network Monitoring Started ---")
    try:
        while True:
            status = check_ping()
            sent,recv = get_network_usage().get("sent"),get_network_usage().get("recv")
            print(f"Status: {status} | Sent: {sent:.2f} MB | Received: {recv:.2f} MB", end="\r")
            time.sleep(3)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    display()
