# Para dormir un thread solo necesitamos importar la libreria time y usar la funcion sleep para pausar por un tiempo la ejecucion del
# thread.

import threading
import time
import logging

logging.basicConfig(
    level=10,
    format='%(thread)s - %(threadName)s: %(message)s'
)

def message():
    logging.info('New Task')
    time.sleep(2)
    logging.info('Task finished')

thread_1 = threading.Thread(target=message)
thread_1.start()