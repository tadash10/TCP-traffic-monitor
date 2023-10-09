import time

class PacketStatistics:
    def __init__(self):
        self.start_time = time.time()
        self.total_packets = 0
        self.packet_count = 0

    def update(self):
        self.packet_count += 1
        current_time = time.time()
        elapsed_time = current_time - self.start_time

        if elapsed_time >= 1.0:
            packets_per_second = self.packet_count / elapsed_time
            self.total_packets += self.packet_count
            self.packet_count = 0
            self.start_time = current_time

            return packets_per_second, self.total_packets

        return None

def calculate_bandwidth(packet):
    # Calculate and return bandwidth usage for the packet
    pass
