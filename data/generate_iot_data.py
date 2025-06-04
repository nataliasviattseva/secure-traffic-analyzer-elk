# Import des bibliothèques nécessaires
import socket
import json
import time
import random
from datetime import datetime

# Fonction qui génère un dictionnaire JSON représentant les mesures d'un capteur
def generate():
    return {
        "timestamp": datetime.now().isoformat(),
        "sensor_id": f"sensor_{random.randint(1, 100)}",
        "location": {
            "lat": round(random.uniform(48.80, 48.90), 6),
            "lon": round(random.uniform(2.30, 2.40), 6)
        },
        "metrics": {
            "temperature": round(random.uniform(10, 35), 1),
            "humidity": round(random.uniform(30, 90), 1),
            "pm2_5": round(random.uniform(0, 150), 1),
            "co2": round(random.uniform(400, 2000), 1)
        }
    }

# Configuration du serveur Logstash destinataire
HOST, PORT = "localhost", 5045

# Création d'une socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur Logstash
sock.connect((HOST, PORT))

# Boucle infinie : envoie des données chaque seconde
try:
    while True:
        message = json.dumps(generate()) + "\n"  # Conversion du dictionnaire en JSON et ajout d'un saut de ligne
        sock.sendall(message.encode())
        time.sleep(1)
except KeyboardInterrupt:
    print("Arrêt de l'envoi.")
finally:
    sock.close()
# Fin du script
