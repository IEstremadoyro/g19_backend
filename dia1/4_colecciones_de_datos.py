# listas se pueden modificar en el tiempo
frutas = ["manzana", "platano", "papaya", "granadilla"]

print(frutas[0])

frutas.append("uva")
print(frutas)

fruta_eliminada = frutas.pop(0)

frutas.remove("papaya")

print(fruta_eliminada)
print(frutas)

frutas[0] = "palta"
print(fruta_eliminada)
print(frutas)

texto = "hola soy su profe"
print(len(frutas))
print(len(texto))


# tuplas no se puedne modificar sus valores
meses = ("enero", "febrero", "marzo")

print(meses[1])

# sets
alumnos = {
    "Abel",
    "Christian",
    "Denys",
    "Andree",
    "Giancarlo",
    "Ignacio",
    "Luis",
    "Segundo",
    "Rodrigo",
    "Renzo"
}

print("Denys" in alumnos)
print("Eduardo" in alumnos)

alumnos.add("Arnold")
# alumnos.remove("luis")
print(alumnos)

# diccionarios
persona = {
    "nombre": "Ignacio",
    "apellido": "Estremadoyro",
    "sexo": "Masculino",
    "hobbies": ["comer", "programar", "Montar bici"],
    "direccion": {
        "calle": "calle 1",
        "numero": 1040,
        "zip_code": "04001"
    },
    "casado": False,
    "estatura": 1.70
}
# para adicionar nuevos campos o actualiar
persona["edad"] = 33
persona["estatura"] = 1.86
print(persona)

print(persona["nombre"])
print(persona["direccion"]["zip_code"])
print(len(persona["hobbies"]))
