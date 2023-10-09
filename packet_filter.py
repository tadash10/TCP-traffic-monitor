def filter_packet(packet, filters):
    src_ip = packet[IP].src
    dst_ip = packet[IP].dst
    src_port = packet[TCP].sport
    dst_port = packet[TCP].dport
    protocol = "TCP" if packet.haslayer(TCP) else "UDP"

    if filters.get("src_ip") and src_ip not in filters["src_ip"]:
        return False
    if filters.get("dst_ip") and dst_ip not in filters["dst_ip"]:
        return False
    if filters.get("src_port") and src_port not in filters["src_port"]:
        return False
    if filters.get("dst_port") and dst_port not in filters["dst_port"]:
        return False
    if filters.get("protocol") and protocol not in filters["protocol"]

    return True
