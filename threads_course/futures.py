# Future en Python es una forma de trabajar con operaciones asíncronas de manera más fácil y eficiente, 
# ya que permite que el programa continúe ejecutándose sin tener que esperar a que la operación asíncrona se complete antes de continuar 
# con otras tareas.

# TODO: leer mas sobre futuros.

# Importe de la libreria para usar future.
from concurrent.futures import Future
from time import sleep
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(thread)s - %(threadName)s: %(message)s'
)
    
# Instancia de la clase Future
future = Future()

# Funcion que se ejecutara cuando el future ya tenga un valor, en este caso una funcion lamda.
# * Nota: la funcion a ejecutar siempre debe recibir un parametro, donde se podria acceder al valor del future.
future.add_done_callback(
    lambda future: logging.info(f'Im the {future.result()}')
)

logging.info('Im a complex task!')
sleep(3)
logging.info('Im finish the complex task!')
logging.info('Im giving value to the future!')
# Valor que se asigna al futuro luego de terminar de ejecutar otras tareas.
future.set_result('Future Value')
logging.info('The future already has value')