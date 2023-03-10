# Es importante saber que podemos instanciar la n cantidad de threads que necesitemos para la ejecucion de nuestro programa.

import threading

def task_1(id):
    for i in range(0, 5):
        print(f'Thread :{id}, Message: {i}')

def task_2(id):
    for i in range(0, 5):
        print(f'Thread :{id}, Message: {i}')

def task_3(id):
    for i in range(0, 5):
        print(f'Thread :{id}, Message: {i}')
        
# Podemos pasar parametros a nuestras funciones de multiples maneras, ya sea usando args o kwargs
# Usando args
# Usando un arreglo
thread_1 = threading.Thread(target=task_1, args=[1])
# Usando una tupla. Es importante poner la coma al final, esto con el fin de que python sepa que es un objeto iterable.
thread_2 = threading.Thread(target=task_2, args=(2,))
# Usando kwargs
# Usando un diccionario usando el nombre del parametro y su funcion
thread_3 = threading.Thread(target=task_3, kwargs={'id': 3})

thread_1.start()
thread_2.start()
thread_3.start()