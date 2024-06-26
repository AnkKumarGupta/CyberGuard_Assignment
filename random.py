from scapy.all import IP, TCP, send, wrpcap
import random

def random_ip():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"

def generate_random_traffic(count=10):
    packets = []
    for _ in range(count):
        packet = IP(src=random_ip(), dst=random_ip())/TCP()
        packets.append(packet)
        send(packet, verbose=0)
    wrpcap('random_addresses.pcap', packets)

generate_random_traffic(count=10)
print("Random complete.")
