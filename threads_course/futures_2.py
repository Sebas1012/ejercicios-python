# !Los futuros son complejos de entender asi que debo leer mas sobre ellos.

from concurrent.futures import Future
import threading
import logging
import requests

logging.basicConfig(
    level=20,
    format='%(thread)s - %(threadName)s: %(message)s'
)

# Genero funcion para realizar una peticion al servidor. Y guardo el valor en un futuro.
def generate_request(url):
    future = Future()

    thread_1 = threading.Thread(target=(
        lambda: future.set_result(requests.get(url))
    ))

    thread_1.start()

    return future

def get_name(response):
    response_json = response.json()
    name = response_json.get('results')[0].get('name').get('first')
    logging.info(f'Random name: {name}')

# Ejecuto la funcion para hacer la peticion
future = generate_request('https://randomuser.me/api')
# Ejecuto una funcion lamda que pasa el valor del futuro a la funcion get_name
future.add_done_callback(
    lambda future: get_name(future.result())
)

# Observo el comportamiento del futuro
while not future.done():
    logging.info('Waiting for an result.')
else:
    logging.info('Finish')