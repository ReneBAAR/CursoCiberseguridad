import socket  # Importamos la librería para conexiones de red

ip_objetivo = '127.0.0.1'
puerto = 22  # SSH

try:
    socket_conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_conexion.settimeout(3)  # Evita que se quede colgado

    socket_conexion.connect((ip_objetivo, puerto))

    banner = socket_conexion.recv(1024)
    banner_texto = banner.decode('utf-8', errors='ignore')

    print(f'Banner del puerto {puerto}:')
    print(banner_texto)

    socket_conexion.close()

except Exception as e:
    print(f'Error al conectarse: {e}')
