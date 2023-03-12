# En este contexto un pool es una forma de controlar la creacion de threds dado a que la creacion de cada uno implica un costo 
# computacional que nos puede jugar en contra en el performance de nuestra app.

# Un pool nos permite limitar el numero de threads que se van a crear pero nos permitira reutilizarlos y asi
# no perder el control de nuestra app.

# Importo la libreria
from concurrent.futures import ThreadPoolExecutor
from time import sleep
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(threadName)s: %(message)s'
)

def add(num_1, num_2):
    sleep(1)
    result = num_1 + num_2
    logging.info(f'{num_1} + {num_2} = {result}')

# Genero un pool con 3 threds que en este caso uno de ellos se va a reutlizar 1 vez,
executor = ThreadPoolExecutor(max_workers=3, thread_name_prefix='Thread')

# Genero 4 ejecuciones de la funcion add.
executor.submit(add, 10, 20)
executor.submit(add, 100, 43)
executor.submit(add, 50, 28)
executor.submit(add, 1, 2)

# Apago el pool, es decir abajo de este no puede existir otro submit.
executor.shutdown()
