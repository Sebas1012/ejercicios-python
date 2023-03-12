from time import sleep
import threading
import logging

logging.basicConfig(
    level=20,
    format='%(thread)s - %(threadName)s: %(message)s'
)

def db_connect():
    logging.info('Connecting to the database...')
    sleep(3)

def get_user():
    logging.info('Getting user...')
    sleep(4)

thread_1 = threading.Thread(target=db_connect)
thread_2 = threading.Thread(target=get_user)

thread_1.start()
thread_2.start()

# Join es un metodo que nos permite decirle al main thread que no se puedo continuar hasta que el thread finalice
thread_1.join()
thread_2.join()

logging.info('Finished threads...')