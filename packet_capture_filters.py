from scapy.all import Ether

def apply_packet_filter(packet, filter_expression):
    try:
        filtered_packet = Ether(packet)
        if filter_expression:
            filtered_packet = filtered_packet.filter(filter_expression)
        return filtered_packet

    except Exception as e:
        return None
