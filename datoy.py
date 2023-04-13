import yaml

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

# Creamos un diccionario con la información
datos = {"nombre": nombre, "apellido": apellido}

# Convertimos el diccionario a formato YAML
yaml_datos = yaml.dump(datos)

# Imprimimos la información en formato YAML
print(yaml_datos)
