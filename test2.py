import pcapy
from scapy.all import IP, TCP
from datetime import datetime

def packet_handler(header, data):
    try:
        eth_frame = IP(data)
        if eth_frame.haslayer(TCP):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            src_ip = eth_frame[IP].src
            dst_ip = eth_frame[IP].dst
            src_port = eth_frame[TCP].sport
            dst_port = eth_frame[TCP].dport

            print(f"[{timestamp}] TCP Packet: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")

    except Exception as e:
        print(f"Error processing packet: {str(e)}")

def main():
    # Replace 'eth0' with the network interface you want to monitor
    interface = 'eth0'

    try:
        cap = pcapy.open_live(interface, 65536, 1, 0)
        print(f"Monitoring TCP traffic on interface {interface}...")

        while True:
            header, data = cap.next()
            packet_handler(header, data)

    except pcapy.PcapError as e:
        print(f"PcapError: {e}")
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
