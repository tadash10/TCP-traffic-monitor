import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime

def visualize_packet_count(packet_counts):
    fig, ax = plt.subplots()

    def animate(i):
        ax.clear()
        ax.plot([str(datetime.now())], packet_counts, label='Packets per second')
        ax.legend()

    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()

if __name__ == "__main__":
    packet_counts = []  # Store packet counts here
    visualize_packet_count(packet_counts)
