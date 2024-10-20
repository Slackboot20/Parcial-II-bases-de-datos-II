import json
import xml.etree.ElementTree as ET

def generar_json(direccion_archivo, datos):
    try:
        with open(direccion_archivo, 'w', encoding='utf-8') as archivo_json:
            json.dump(datos, archivo_json, indent=4, ensure_ascii=False)
        print(f"El archivo JSON fue creado con éxito.")
    except Exception as e:
        print(f"Ocurrió un error al crear el archivo JSON: {e}")

def generar_xml(direccion_archivo, datos):
    try:
        empleado = ET.Element("empleado")

        for clave, valor in datos.items():
            elemento = ET.SubElement(empleado, clave)
            elemento.text = str(valor)

        arbol = ET.ElementTree(empleado)
        arbol.write(direccion_archivo, encoding='utf-8', xml_declaration=True)
        print(f"El archivo XML fue creado con éxito.")
    except Exception as e:
        print(f"Ocurrió un error al crear el archivo XML: {e}")

def ingresar_datos():
    datos = {}

    nombre = str(input("Ingrese el nombre del empleado: "))
    edad = int(input("Ingrese la edad del empleado: "))
    departamento = str(input("Ingrese el departamento de residencia: "))
    salario = int(input("Ingrese el salario: "))

    datos["nombre"] = nombre
    datos["edad"] = edad
    datos["departamento"] = departamento
    datos["salario"] = salario

    return datos

direccion_json = r"C:\Users\Camil\OneDrive\Escritorio\Bases de datos II\Parcial II\Punto 1\Empleados.json"
direccion_xml = r"C:\Users\Camil\OneDrive\Escritorio\Bases de datos II\Parcial II\Punto 1\Empleados.xml"

datos_ingresados = ingresar_datos()
generar_json(direccion_json, datos_ingresados)
generar_xml(direccion_xml, datos_ingresados)