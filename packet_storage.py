import json

def save_packet_to_json(packet, output_file):
    with open(output_file, 'a') as file:
        packet_data = {
            "timestamp": str(datetime.now()),
            "src_ip": packet[IP].src,
            "dst_ip": packet[IP].dst,
            "src_port": packet[TCP].sport,
            "dst_port": packet[TCP].dport,
            "payload": str(packet[TCP].payload)
        }
        file.write(json.dumps(packet_data) + '\n')
