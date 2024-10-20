import xml.etree.ElementTree as ET
import json

def exportar_a_json(direccion_xml, direccion_json):

    arbol = ET.parse(direccion_xml)
    raiz = arbol.getroot()

    productos = []

    for producto in raiz.findall("productos"):
        prod_dict = {
            "id": producto.get("id"),
            "nombre": producto.find("nombre").text,
            "descripcion": producto.find("descripcio").text,
            "precio": producto.find("precio").text,
            "stock": producto.find("stock").text
        }
        productos.append(prod_dict)

    with open(direccion_json, 'w', encoding='utf-8') as archivo_json:
        json.dump(productos, archivo_json, indent=4, ensure_ascii=False)

    print(f"Datos exportados a {direccion_json} con exito.")

direccion_archivo = r"punto2/catalogo.xml"
direccion_json = r"punto2/catalogo.json"
exportar_a_json(direccion_archivo, direccion_json)