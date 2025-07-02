import csv
import random
from datetime import datetime, timedelta

# Paramètres
NUM_LOGS = 1000
CSV_FILE = "network_security_logs.csv"

# Valeurs possibles
PROTOCOLS = ["TCP", "UDP", "ICMP", "HTTP", "HTTPS"]
ACTIONS = ["ALLOW", "BLOCK", "DROP"]
THREAT_LEVELS = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]

# Génération de logs
def generate_log_entry(base_time):
    return {
        "timestamp": (base_time + timedelta(seconds=random.randint(0, 3600))).strftime("%Y-%m-%d %H:%M:%S"),
        "source_port": random.randint(1024, 65535),
        "destination_port": random.randint(1, 1024),
        "protocol": random.choice(PROTOCOLS),
        "action": random.choice(ACTIONS),
        "bytes_sent": random.randint(0, 5000),
        "bytes_received": random.randint(0, 10000),
        "threat_level": random.choices(
            THREAT_LEVELS, weights=[60, 25, 10, 5], k=1
        )[0],  # plus de chances d'avoir LOW/MEDIUM
    }

# Écriture dans le fichier CSV
with open(CSV_FILE, mode="w", newline="") as file:
    fieldnames = [
        "timestamp",
        "source_port",
        "destination_port",
        "protocol",
        "action",
        "bytes_sent",
        "bytes_received",
        "threat_level",
    ]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    base_time = datetime.now()

    for _ in range(NUM_LOGS):
        log = generate_log_entry(base_time)
        writer.writerow(log)

print(f"{NUM_LOGS} logs générés dans le fichier : {CSV_FILE}")
# Fin du script