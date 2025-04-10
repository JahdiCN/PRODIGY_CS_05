from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime

def process_packet(packet):
    print("=" * 60)
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Check if packet has IP layer
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto = ip_layer.proto

        # Determine protocol
        if proto == 6:
            protocol = "TCP"
        elif proto == 17:
            protocol = "UDP"
        elif proto == 1:
            protocol = "ICMP"
        else:
            protocol = f"Other ({proto})"

        print(f"Source IP      : {src_ip}")
        print(f"Destination IP : {dst_ip}")
        print(f"Protocol       : {protocol}")

        # Show payload if it exists
        if Raw in packet:
            payload = packet[Raw].load
            print(f"Payload (raw)  : {payload[:100]!r}")  # Show only first 100 bytes
        else:
            print("Payload        : None")
    else:
        print("Non-IP packet received.")

def start_sniffing(interface=None):
    print("Starting packet sniffing... (Press Ctrl+C to stop)")
    sniff(prn=process_packet, iface=interface, store=False)

if __name__ == "__main__":
    # For default interface, pass nothing to start_sniffing()
    # Replace 'eth0' or 'Wi-Fi' with your actual interface name if needed
    start_sniffing()
