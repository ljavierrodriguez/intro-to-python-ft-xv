""" a, b = 1, 2

print(a)
print(b)

nombres = ["Hugo", "Paco", "Luis", "Donald", "Smith"]

a, b, c, _, e = nombres # _ ignora el valor """

""" print(a)
print(b)
print(c)
print(e) """

""" a = nombres[0:2]
b = nombres[2:]

print(a)
print(b) """

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista[0::2])

range(0, 10, 1)

first, second, *rest = lista

print(first, second, rest)


listado = [
    { "nombre": "Santiago", "nota": 12 }, 
    { "nombre": "Aziel", "nota": 18 }, 
    { "nombre": "Maria", "nota": 7}, 
    { "nombre": "Anyelina", "nota": 30}, 
    { "nombre": "Cristian", "nota": 22}, 
    { "nombre": "Joaquin", "nota": 12}, 
    { "nombre": "Benjamin", "nota": 15}, 
    { "nombre": "David", "nota": 11}, 
    { "nombre": "Anna", "nota": 10}
]


for estudiante in listado:
    print(estudiante["nombre"])

notas = [est["nota"] for est in listado if est["nombre"] != "Anna"]
print(notas)

""" listado = list(filter(lambda est:  est["nombre"] != "Anna", listado))
print(listado) """

notas = list(map(lambda est: est["nota"], list(filter(lambda est:  est["nombre"] != "Anna", listado))))
print(notas)

