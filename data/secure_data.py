import socket
import json
import time
import csv

HOST = 'localhost'
PORT = 5045

with open('traffic_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        for row in reader:
            s.sendall((json.dumps(row) + "\n").encode('utf-8'))
            time.sleep(1)  # pour simuler un flux continu
