import requests
# Libreria para poder usar threads
import threading

def get_name():
    response = requests.get('https://randomuser.me/api')

    if response.status_code == 200:
        data = response.json().get('results')
        name = data[0].get('name').get('first')
        
        print(name)

for i in range(0, 20):
    # Creacion de un thread
    thread = threading.Thread(target=get_name)
    # Inicio de un thread
    thread.start()


