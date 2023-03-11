def validate_username(username):
    if len(username) < 5:
        # Raise levanta una excepcion, y ayudandonos de la clase Exception() podemos dar mas contexto.
        raise Exception('Length less than 5 characters')
    
    return True

try:
    username = validate_username('test')
except Exception as error:
    print(f'An error occurred: {error}')
else:
    print(username)
