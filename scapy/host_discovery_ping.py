from scapy.all import *

ip = IP()
icmp = ICMP()
pingPckt = ip/icmp

addr = "10.10.10."
ipList = []

for i in range(125, 256):
    pingPckt[IP].dst=addr+str(i)
    response = sr1(pingPckt,timeout=0.5, verbose=False)  # Timeout süresini artırabilirsiniz
    if (response):
         #print(pingPckt[IP].dst, "is up")
        ipList.append(pingPckt[IP].dst)
    else:
        pass

print(ipList)