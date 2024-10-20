import json
import xml.etree.ElementTree as ET

# Función para leer JSON
def leer_json(direccion_archivo):
    try:
        with open(direccion_archivo, 'r', encoding='utf-8') as archivo_json:
            datos = json.load(archivo_json)
            return datos
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo JSON: {e}")
        return None

# Función para guardar JSON
def guardar_json(direccion_archivo, datos):
    try:
        with open(direccion_archivo, 'w', encoding='utf-8') as archivo_json:
            json.dump(datos, archivo_json, indent=4, ensure_ascii=False)
        print(f"Parámetro agregado con éxito en JSON.")
    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo JSON: {e}")

# Función para leer XML
def leer_xml(direccion_archivo):
    try:
        tree = ET.parse(direccion_archivo)
        root = tree.getroot()

        # Convertir los datos del XML en un diccionario
        datos = {}
        for elemento in root:
            datos[elemento.tag] = elemento.text

        return datos
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo XML: {e}")
        return None

# Función para guardar XML
def guardar_xml(direccion_archivo, datos):
    try:
        # Crear el elemento raíz
        empleado = ET.Element("empleado")

        # Crear subelementos con los datos actualizados
        for clave, valor in datos.items():
            elemento = ET.SubElement(empleado, clave)
            elemento.text = str(valor)

        # Crear el árbol XML y escribirlo en un archivo
        arbol = ET.ElementTree(empleado)
        arbol.write(direccion_archivo, encoding='utf-8', xml_declaration=True)
        print(f"Parámetro agregado con éxito en XML.")
    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo XML: {e}")

# Función para agregar un nuevo parámetro
def agregar(nombre_archivo, formato):
    if formato == 'json':
        datos = leer_json(nombre_archivo)
    elif formato == 'xml':
        datos = leer_xml(nombre_archivo)
    else:
        print("Formato no soportado.")
        return

    if datos is not None:
        clave = str(input("Ingrese el nuevo parámetro: "))
        valor = str(input("Ingrese el valor para el nuevo parámetro: "))

        datos[clave] = valor

        if formato == 'json':
            guardar_json(nombre_archivo, datos)
        elif formato == 'xml':
            guardar_xml(nombre_archivo, datos)
    else:
        print("No fue posible la actualización.")

# Dirección de los archivos
direccion_json = r"C:\Users\Camil\OneDrive\Escritorio\Bases de datos II\Parcial II\Punto 1\Empleados.json"
direccion_xml = r"C:\Users\Camil\OneDrive\Escritorio\Bases de datos II\Parcial II\Punto 1\Empleados.xml"

# Elegir el archivo a modificar y su formato (json o xml)
formato_archivo = str(input("¿Desea modificar el archivo 'json' o 'xml'?: "))
if formato_archivo == 'json':
    agregar(direccion_json, formato_archivo)
elif formato_archivo == 'xml':
    agregar(direccion_xml, formato_archivo)
else:
    print("Formato no válido.")