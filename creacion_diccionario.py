""""
Requerimos crear un registro de datos personales de tres personas. Los datos que se necesitan son: 
su nombre, apellido y teléfono. Para ello, generaremos un diccionario para cada una de las personas 
con los datos mencionados, y luego los almacenaremos dentro de una lista. Finalmente, 
imprimiremos en pantalla la lista.
"""
usuario1= {'nombre': 'Tamara', 'apellido': 'González', 'telefono': 978567834}
usuario2= {'nombre': 'Santiago', 'apellido': 'Reyes', 'telefono': 989654734}
usuario3= {'nombre': 'Andres', 'apellido': 'Durant', 'telefono': 945688331}

lista_usuarios= (usuario1, usuario2, usuario3)

print(lista_usuarios)
print("")
for l in lista_usuarios:
    print('--------------')
    print('\t Nombre:', l['nombre'])
    print('\t Apellido:', l['apellido'])
    print('\t Telefono:', l['telefono'])