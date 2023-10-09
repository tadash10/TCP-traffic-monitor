import pcapy
from scapy.all import IP, TCP
from packet_filter import filter_packet
from logging_handler import setup_logger, log_packet
from packet_stats import PacketStatistics
from alerting import PacketAlerting

def packet_handler(header, data, logger, filters, stats, alerting):
    try:
        eth_frame = IP(data)
        if eth_frame.haslayer(TCP):
            packet = f"TCP Packet: {eth_frame[IP].src}:{eth_frame[TCP].sport} -> {eth_frame[IP].dst}:{eth_frame[TCP].dport}"
            log_packet(logger, packet)
            
            if filter_packet(eth_frame, filters):
                packets_per_second, total_packets = stats.update()
                if packets_per_second is not None:
                    print(f"Packets per second: {packets_per_second:.2f} | Total packets: {total_packets}")
                
                if alerting.check_alert(eth_frame):
                    print("Alert: Unusual traffic detected!")

    except Exception as e:
        logger.error(f"Error processing packet: {str(e)}")

if __name__ == "__main__":
    interface = 'eth0'
    log_file = 'packet_log.txt'

    logger = setup_logger(log_file)
    filters = {
        "src_ip": ["192.168.1.1"],
        "dst_ip": ["8.8.8.8"],
        "protocol": ["TCP"]
    }
    stats = PacketStatistics()
    alerting = PacketAlerting()

    try:
        cap = pcapy.open_live(interface, 65536, 1, 0)
        print(f"Monitoring TCP traffic on interface {interface}...")

        while True:
            header, data = cap.next()
            packet_handler(header, data, logger, filters, stats, alerting)

    except pcapy.PcapError as e:
        logger.error(f"PcapError: {e}")
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {str(e)}")
