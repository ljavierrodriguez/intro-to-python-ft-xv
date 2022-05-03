'''
Comentario Multiples Lineas

Datos Primitivos

String
Int
Float
Boolean

Datos No Primitivo

Function
Lista
Tuples
Sets
Dict

And = and
Or = or
Not = not

'''
# Comentario Simple

nombre = ''' Lorem Ipsum es simplemente el texto de relleno de las imprentas y 
archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de 
las industrias desde el año 1500, cuando un impresor (N. del T. persona que se 
dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal 
manera que logró hacer un libro de textos especimen. 
'''

edad = 34 # int

precio = 34.5 # Float

flag = True or False

estudiantes = [1, 2, 3] # list
#estudiantes2 = list(1,2,3)

estatus = ("activo", "inactivo", "cancelado", "suspendido", "pendiente") # tuple

frutas = { "manzana", "pera", "uvas", "banana" } # set

apellido = None


print(dir(estatus))

persona = {
    'nombre': 'Luis',
    'apellido': 'Rodriguez'
} # dict

print(dir(persona))