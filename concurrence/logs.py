import logging

# Niveles de mensajes:
# Debug(10) - Info(20) - Warning(30) - Error(40) - Critical(50)

# Configuracion de nuestros mensaje de logging
logging.basicConfig(
    # Level permite configurar apartir de que nivel queremos mostrar los mensajes
    level=10,
    # Format permite darle formato al texto de salida de los mensajes
    format= '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s',
    # Permite guardar los mensajes en un archivo de texto
    filename= 'logs.txt'
)

def messages():
    # Definicion de nuestros diferentes mensajes de logging.
    logging.debug('Mensaje de Debug')
    logging.info('Mensaje de Info')
    logging.warning('Mensaje de Warning')
    logging.error('Mensaje de Error')
    logging.critical('Mensaje de Critical')

if __name__ == '__main__':
    messages()