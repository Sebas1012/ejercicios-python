import threading
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(threadName)s: %(message)s'
)

# La clase lock permite controlar el acceso de un thread a un espacio en memoria, esto con el fin de evitar errores
# como el Race Condition que se produce cuando multiples threads acceden a un mismo recurso.
# Lock lo que hace es que mientras un thread tenga ocupado el recurso, otro no podra acceder al mismo hasta que ese thread libere el recurso.
lock = threading.Lock()

BALANCE = 0

def deposit():
    global BALANCE

    for _ in range(0, 1000000):
        # Forma de bloquear el recurso usando contexto
        with lock:
            BALANCE +=1  # Seccion Critica

def removals():
    global BALANCE

    for _ in range(0, 1000000):
        # forma de bloquear el acceso al recurso usando el metodo acquire y release
        # acquire -> Accede al recurso
        lock.acquire()
        BALANCE -=1 # Seccion Critica
        # release -> Libera el recurso
        lock.release()

thread_1 = threading.Thread(target=deposit)
thread_2 = threading.Thread(target=removals)

thread_1.start()
thread_2.start()

logging.info(f'Final balance value is: {BALANCE}')


# Es importante tener en cuenta que lock solo permite acceder una sola vez al recurso y para volver a acceder, el mismo debe estar ya liberado
# para solucionar eso en vez de instancia Lock, instanciamos RLock() y ya deberiamos poder acceder al recurso las veces que necesitos antes de 
# liberarlo, pero es importante que el numero de veces que sea accedido, tambien sea liberado, ejemplo:

    # lock.acquire() # Estado: Ocupado

    # lock.acquire() # A la espera de que sea liberado

    # BALANCE -= 10

    # lock.release()

    # lock.release()

# Lo accedo 2 veces y lo libero 2 veces