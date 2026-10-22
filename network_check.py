
import socket

# Adresse IP de la machine locale
host = "127.0.0.1"

# Demande le port à vérifier
port = int(input("Enter port number: "))

# Crée une socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Définit un délai maximal de 2 secondes
    sock.settimeout(2)

    # Essaie de se connecter au port indiqué
    result = sock.connect_ex((host, port))

# Affiche le résultat du test
if result == 0:
    print("Port is open")
else:
    print("Port is closed or unreachable")
