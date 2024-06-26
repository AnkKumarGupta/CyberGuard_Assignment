from scapy.all import sniff, wrpcap

def capture_packets(filename, count=10):
    packets = sniff(count=count)
    wrpcap(filename, packets)

capture_packets('actual.pcap', count=10)
print("Actual completed")
