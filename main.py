"""
Proyecti Python y Mysql
Login o registro
si elegimos registro, creara un usuario en la bbdd
si elegimos login, identificara al usuario y nos preguntará
Crear nota, mostrar notas, borrarlas.

"""
from usuarios import acciones

print("""
Acciones disponibles
    - registro
    - login
""")

hasEl = acciones.Acciones()

accion = input("¿Que quieres hacer?: ")

if accion == "registro":
  hasEl.registro()  

elif accion == "login":
    hasEl.login()