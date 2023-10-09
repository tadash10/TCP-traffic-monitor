from scapy.all import TCP, UDP, DNS, HTTP

def decode_packet_payload(packet):
    payload = None

    if packet.haslayer(TCP):
        payload = decode_tcp_packet(packet)
    elif packet.haslayer(UDP):
        payload = decode_udp_packet(packet)

    return payload

def decode_tcp_packet(packet):
    if packet.haslayer(HTTP):
        # Extract and analyze HTTP request
        http_payload = packet[HTTP].payload
        return f"HTTP Request: {http_payload.decode('utf-8', 'ignore')}"

    # Handle other application-layer protocols as needed
    return None

def decode_udp_packet(packet):
    if packet.haslayer(DNS):
        # Extract and analyze DNS query
        dns_query = packet[DNS].qd.qname
        return f"DNS Query: {dns_query.decode('utf-8', 'ignore')}"

    # Handle other application-layer protocols as needed
    return None
