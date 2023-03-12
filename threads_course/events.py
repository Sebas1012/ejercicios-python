# Loes events son una manera de comunicarnos con los threads y hacer que se ejecuten o continuen un proceso cuando les demos una señal.

import logging
import threading
from time import sleep

logging.basicConfig(
    level=logging.INFO,
    format='%(threadName)s: %(message)s'
)

def task_1(event):
    logging.info('Im a task 1')
    logging.info('Waiting for a signal')
    # Esperamos a que se setee la señal a True
    event.wait()
    logging.info('Signal sent')

def task_2(event):
    logging.info('Im a task 2')

# Instanciamos
event = threading.Event()

thread_1 = threading.Thread(target=task_1, args=(event, ))
thread_2 = threading.Thread(target=task_2, args=(event, ))

thread_1.start()
thread_2.start()

sleep(4)

# Damos la señal, es decir cambiamos su valor por defecto, que es False a True
event.set()