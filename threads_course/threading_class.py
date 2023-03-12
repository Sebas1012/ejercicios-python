import threading
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(thread)s - %(threadName)s: %(message)s'
)

def thread_info():
    # Obtener informacion del thread en el que se esta ejecutando la tarea
    currentThread = threading.current_thread()
    # Obtener el nombre del thread en el que se esta ejecutando la tarea
    name = currentThread.getName
    # Obtener el ID del thread en el que se esta ejecutando la tarea.
    id = threading.get_ident()

    logging.info(f'Current Thred is: {currentThread} - Thread Name: {name} - Thread ID: {id}')

# Con el parametro name= podemos poner un nombre custom al thread que creamos
thread_1 = threading.Thread(target=thread_info, name='thread-custom')
thread_1.start()

# Con enumerate podemos ver todos los threads que estan en ejecucion
logging.info(f'Live threads: {threading.enumerate()}')