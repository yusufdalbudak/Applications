Host Discovery Tool 
Overview

This Host Discovery Tool is a simple Python script created to perform host discovery on a specified network using Scapy, a powerful packet manipulation library.
Features

    Ping-based Host Discovery: Utilizes ICMP (ping) packets to identify live hosts on the network.
    ARP-based Host Discovery: Utilizes ARP (Address Resolution Protocol) packets to discover hosts on the local network.

Prerequisites

    Python 3.x
    Scapy library (pip install scapy)

Usage
Ping-based Host Discovery
python host_discovery_ping.py
Edit the script to define the target IP range.
Adjust the timeout parameter as needed.

ARP-based Host Discovery
python host_discovery_arp.py
    Edit the script to set the destination MAC address and target IP range.
    Adjust the timeout parameter as needed.

    Results

    The tool will display a list of live hosts discovered during the scanning process.
    Examples
Ping-based Host Discovery
Examples
Ping-based Host Discovery

ARP-based Host Discovery
python host_discovery_arp.py



Notes

    Ensure that you have the necessary permissions to send and receive packets on the network.
    Use responsibly and only on networks you have explicit permission to scan.

Disclaimer

This tool is provided as-is, without any warranty or guarantees. Use at your own risk.
Contributing

Contributions are welcome! If you find issues or have suggestions, please open an issue or create a pull request.
