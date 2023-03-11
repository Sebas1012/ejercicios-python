# En programación, una excepción es un evento que ocurre durante la ejecución de un programa que interrumpe el flujo normal de la misma. 
# Cuando ocurre una excepción, el programa deja de ejecutarse en su punto actual y busca un "manejador de excepciones" que pueda manejar 
# el error y continuar la ejecución normal del programa.

# Para trabajar con excepciones en python, se usan los bloques try: y except:

# try -> Codigo que puede generar una excepcion
# except -> Codigo que se ejecutara en caso de que el codigo de try falle.

try:
    number_1 = 5
    number_2 = 0

    # Linea de codigo que lanzara la excepcion.
    result = number_1 / number_2

    print(f'Result: {result}')

# Como buena practica se recomienda especificar el tipo de error esperado en el bloque except.
except ZeroDivisionError as error:
    print(f'An error occurred: {error}')

# En caso de que hayan mas posibles errores, podemos agregarlos
except NameError as error:
    print(f'Variable does not exist: {error}')


try:
    array = [1, 2, 3, 4]

    # Linea de codigo que lanzara la excepcion.
    result = [4]

# En caso de que queramos ser mas generales con cualquier tipo de error usamos la clase Exception
except Exception as error:
    print(f'An error occurred: {error}')