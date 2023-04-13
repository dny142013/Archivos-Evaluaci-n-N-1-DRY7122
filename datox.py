from xml.etree.ElementTree import Element, SubElement, tostring

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

# Creamos el elemento raíz del documento XML
raiz = Element("persona")

# Creamos los elementos "nombre" y "apellido" y les asignamos los valores ingresados por el usuario
elem_nombre = SubElement(raiz, "nombre")
elem_nombre.text = nombre
elem_apellido = SubElement(raiz, "apellido")
elem_apellido.text = apellido

# Convertimos el árbol de elementos en una cadena en formato XML
xml_datos = tostring(raiz, encoding="unicode")

# Imprimimos la información en formato XML
print(xml_datos)
