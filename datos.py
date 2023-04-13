import json

n = input ("Ingrese su nombre:" )
a = input ("Ingrese su apellido: " )

# Creamos un diccionario con la información
informacion = {"nombre": n, "apellido": a}

# Convertimos el diccionario a formato JSON
json_informacion = json.dumps(informacion)

# Imprimimos el resultado
print(json_informacion)
