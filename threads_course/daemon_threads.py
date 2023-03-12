# Un deamon thread es un thread que depende de mainthred para finalizar su ejecucion, es decir,
# se ejecutara en segundo plano mientras la ejecucion del main thread finaliza, cuand eso pase
# el daemon thread tambien lo hara.

import threading
from time import sleep
import logging

logging.basicConfig(
    level=20,
    format='%(thread)s - %(threadName)s: %(message)s'
)

# Genero una funcion que nos imprimira un mensaje de manera infinita
def daemon_thread():
    while True:
        logging.info('Im a daemon thread!')
        sleep(0.5)

# Genero el demonio con el parametro daemon=True
thread_1 = threading.Thread(target=daemon_thread, daemon=True)
thread_1.start()

# Finalizo el MainThread al precionar una tecla
input('Press a key to end the Main Thread')

logging.info('Main Thread terminated')