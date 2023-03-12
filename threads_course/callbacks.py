# Un callback se refiere a una función que se pasa como argumento a otra función y que se llama dentro de la función principal en un 
# momento específico.

import threading
import logging
import requests

logging.basicConfig(
    level=20,
    format='%(thread)s - %(threadName)s: %(message)s'
)

def generate_request(url, success_callback, error_callback):
    response = requests.get(url)

    if response.status_code == 200:
        # Callback
        success_callback(response.json())
    else:
        # Callback
        error_callback()

# Funcion que se eecutara en caso de que todo salga bien.
def get_name(response_json):
    name = response_json.get('results')[0].get('name').get('first')
    logging.info(f'Random name is: {name}')

def get_pokemon(response_json):
    pokemon = response_json.get('forms')[0].get('name')
    logging.info(f'Random pokemon is: {pokemon}')

def message():
    logging.info('Im a callback...Im waiting 3 secobnds')

# Funcion que se eecutara en caso de que todo salga mal.
def error():
    logging.error('Error')

thread_1 = threading.Thread(target=generate_request, kwargs={'url': 'https://randomuser.me/api',
                                                             'success_callback': get_name,
                                                             'error_callback': error})

thread_2 = threading.Thread(target=generate_request, kwargs={'url': 'https://pokeapi.co/api/v2/pokemon/1/',
                                                             'success_callback': get_pokemon,
                                                             'error_callback': error})

# La clase timer nos permite retrasar o definir al pasado cuanto tiempo queremos ejecutar un callback/funcion
thread_3 = threading.Timer(3, message)

thread_1.start()
thread_2.start()
thread_3.start()

