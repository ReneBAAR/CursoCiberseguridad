usuario_logueado = True
es_admin = True

if usuario_logueado:
    print("Bienvenido al sistema.")
    
    if es_admin:
        print("Tienes acceso completo a la configuración.")
        
    else:
        print("Acceso de usuario estándar.")
    
else:
    print("Por favor, inicia sesión para continuar.")