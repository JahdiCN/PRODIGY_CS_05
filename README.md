# NETWORK PACKET ANALYZER
# 🕵️ Packet Sniffer Tool (Built with Python + Scapy)

This is a simple yet powerful packet sniffer tool built using Python and the Scapy library. It captures and displays real-time network packets, including source and destination IP addresses, protocol types, and raw payload data.

---

## 🚀 Features

- Captures real-time packets on your network interface
- Displays:
  - Source IP address
  - Destination IP address
  - Protocol (TCP, UDP, ICMP, etc.)
  - Payload (if available)
- Easy to use and extend
- Great for learning network analysis

---

## 📦 Requirements

- Python 3.6+
- [Scapy](https://scapy.net/)
- [Npcap](https://nmap.org/npcap/) (for Windows users)

---

## 🔧 Installation

1. **Clone this repository**

```bash
git clone https://github.com/yourusername/packet-sniffer.git
cd packet-sniffer
```
## Output
```sh
============================================================
Time: 2025-04-10 17:40:52
Source IP      : 192.168.1.5
Destination IP : 192.168.1.1
Protocol       : TCP
Payload (raw)  : b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n'
```
## 📄Liscence
This project is licensed under the MIT License.

