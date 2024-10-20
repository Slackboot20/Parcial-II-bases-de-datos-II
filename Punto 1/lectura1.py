import json
import xml.etree.ElementTree as ET

def leer_json(direccion_archivo):
    try:
        with open(direccion_archivo, 'r', encoding='utf-8') as archivo_json:
            datos = json.load(archivo_json)
            return datos
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo JSON: {e}")
        return None

def leer_xml(direccion_archivo):
    try:
        tree = ET.parse(direccion_archivo)
        root = tree.getroot()

        datos = {}
        for elemento in root:
            datos[elemento.tag] = elemento.text

        return datos
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo XML: {e}")
        return None

direccion_json = r"C:\Users\Camil\OneDrive\Escritorio\Bases de datos II\Parcial II\Punto 1\Empleados.json"
direccion_xml = r"C:\Users\Camil\OneDrive\Escritorio\Bases de datos II\Parcial II\Punto 1\Empleados.xml"

lectura_datos_json = leer_json(direccion_json)
if lectura_datos_json:
    print("Datos del archivo JSON:")
    print(json.dumps(lectura_datos_json, indent=4, ensure_ascii=False))

lectura_datos_xml = leer_xml(direccion_xml)
if lectura_datos_xml:
    print("\nDatos del archivo XML:")
    print(lectura_datos_xml)