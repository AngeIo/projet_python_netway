import socket

server="127.0.0.1"
mysocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def portscanning(port):
    try:  # Gestion de l'exception
        mysocket.connect((server, port))         
        return True
    except:         
        # Si erreur de connexion sur le serveur alors :
        return False
    mysocket.close()
      
for port in range(135,150):  #Valeur pouvant aller de 1 à 65536
    if scandeport(port):
        print("port", port, "is open.")
    else: 
        print("port", port, "is closed.")
        continue
        

