
import socket

# Adresse IP de la machine locale : les tests restent sur ton propre ordinateur
host = "127.0.0.1"

# Demande à l'utilisateur de saisir le port à vérifier
# input() récupère du texte et int() le convertit en entier
port = int(input("Enter port number: "))

# Crée une socket TCP pour tester la connexion au port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

    # Définit un délai maximal de 2 secondes pour la connexion
    sock.settimeout(2)

    # Essaie de se connecter au port indiqué
    # connect_ex() renvoie 0 si la connexion réussit
    result = sock.connect_ex((host, port))

# Affiche le résultat du test
if result == 0:
    print("Port is open")
else:
    print("Port is closed or unreachable")
