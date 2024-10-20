import json
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Función para leer el JSON
def leer_json(direccion_archivo):
    try:
        with open(direccion_archivo, 'r', encoding='utf-8') as archivo_json:
            datos = json.load(archivo_json)
            return datos
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo JSON: {e}")
        return None

# Función para convertir los datos en formato XML
def generar_resumen_xml(datos):
    # Crear el elemento raíz
    root = ET.Element("resumenEncuestas")

    for encuesta in datos:
        # Crear un elemento para cada ciudad
        ciudad_elem = ET.SubElement(root, "ciudad", nombre=encuesta["ciudad"])

        # Agregar el número de personas encuestadas
        personas_elem = ET.SubElement(ciudad_elem, "personasEncuestadas")
        personas_elem.text = str(encuesta["personas_encuestadas"])

        # Crear un subelemento para los tipos de transporte
        transportes_elem = ET.SubElement(ciudad_elem, "transportes")

        for transporte in encuesta["transporte_utilizado"]:
            transporte_elem = ET.SubElement(transportes_elem, "transporte", tipo=transporte["transporte"])
            cantidad_elem = ET.SubElement(transporte_elem, "cantidad")
            cantidad_elem.text = str(transporte["cantidad"])

    # Convertir el árbol en una cadena XML y devolverlo
    return ET.tostring(root, encoding="unicode", method="xml")

# Función para guardar el XML en un archivo
def guardar_xml(direccion_archivo, contenido_xml):
    try:
        with open(direccion_archivo, 'w', encoding='utf-8') as archivo_xml:
            archivo_xml.write(contenido_xml)
            print(f"Archivo XML guardado en: {direccion_archivo}")
    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo XML: {e}")

# Función para formatear el XML
def formatear_xml(contenido_xml):
    dom = minidom.parseString(contenido_xml)
    return dom.toprettyxml(indent="  ")  # Indentar con dos espacios

# Dirección del archivo JSON
direccion_json = r"C:\Users\Camil\OneDrive\Escritorio\Bases de datos II\Parcial II\Punto3\Encuestas.json"
# Dirección del archivo XML donde se guardará el resumen
direccion_xml = r"C:\Users\Camil\OneDrive\Escritorio\Bases de datos II\Parcial II\Punto3\resumen_encuestas.xml"

# Leer el archivo JSON
datos_json = leer_json(direccion_json)

# Si se leen los datos correctamente, generar el resumen en XML
if datos_json:
    resumen_xml = generar_resumen_xml(datos_json)
    
    # Formatear el contenido XML para la impresión
    resumen_xml_formateado = formatear_xml(resumen_xml)
    
    # Imprimir el contenido XML formateado en consola
    print(resumen_xml_formateado)
    
    # Guardar el contenido XML en un archivo
    guardar_xml(direccion_xml, resumen_xml)