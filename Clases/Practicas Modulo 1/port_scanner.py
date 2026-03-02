import socket  # Importamos la librería para conexiones de red

# Definimos la IP objetivo
ip_objetivo = '192.168.1.5'  # localhost (tu propia computadora)

# Definimos el rango de puertos a escanear
puerto_inicio = 1
puerto_fin = 100

# Creamos un bucle para probar cada puerto
for puerto in range(puerto_inicio, puerto_fin + 1):
    # Intentamos conectarnos
    try:
        socket_conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        resultado = socket_conexion.connect_ex((ip_objetivo, puerto))
        
        if resultado == 0:
            print(f'Puerto {puerto}: ABIERTO')
        
        socket_conexion.close()
    except:
        print(f'Error al escanear puerto {puerto}')