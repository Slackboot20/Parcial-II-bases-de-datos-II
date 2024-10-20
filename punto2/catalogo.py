import xml.etree.ElementTree as ET

def crear_catalogo_xml(direccion_archivo):
    catalogo = ET.Element("catalogo")

    productos = [
        {"id":"1", "nombre":"Laptop", "descripcion":"Laptop Dell Inspiron", "precio":"2000000", "stock":"50"},
        {"id":"2", "nombre":"Mouse", "descripcion":"Mouse inlamabrico Logitech", "precio":"60000", "stock":"50"},
        {"id":"3", "nombre":"Teclado", "descripcion":"Teclado mecanico Corsair", "precio":"120000", "stock":"50"},
        {"id":"4", "nombre":"Monitor", "descripcion":"Monito LG 24 pulgadas", "precio":"1500000", "stock":"50"},
        {"id":"5", "nombre":"Impresora", "descripcion":"Impresora HP LaseJet", "precio":"3000000", "stock":"50"},
    ]

    for producto in productos:

        prod = ET.SubElement(catalogo, "productos", id=producto["id"])
        ET.SubElement(prod, "nombre").text = producto["nombre"]
        ET.SubElement(prod, "descripcio").text = producto["descripcion"]
        ET.SubElement(prod, "precio").text = producto["precio"]
        ET.SubElement(prod, "stock").text = producto["stock"]

    arbol = ET.ElementTree(catalogo)
    arbol.write(direccion_archivo, encoding='utf-8', xml_declaration=True)

direccion_archivo = r"punto2/catalogo.xml"
crear_catalogo_xml(direccion_archivo)
print(f"Archivo {direccion_archivo} creado con exito.")
        