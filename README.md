# CyberGuard_Assignment

Generated Two Files, first is random.pcap by executing the code file random.py and the second is actual.pcap by executing the code file actual.py, both with a count of 10 packets.

On analyzing actual.pcap using Wireshark, tried to find out some suspicious instances and the one which I suspected is that There is an abrupt 46 seconds delay while loading 6th to 7th packet, it might be an indication of some suspicious activity.

On analyzing random.pcap using Wireshark, I found that all the 10 packets generated are TCP SYN Packets, as all the packets are SYN packets, there might be a possibility of SYN Flood Attack.
