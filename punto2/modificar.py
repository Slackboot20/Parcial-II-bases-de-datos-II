import xml.etree.ElementTree as ET

def mostrar_productos_disponibles(direccion_archivo):
    try:
        arbol = ET.parse(direccion_archivo)
        raiz = arbol.getroot()

        print("Productos disponibles:")
        for producto in raiz.findall("productos"):
            print(f"- ID: {producto.get('id')}, Nombre: {producto.find('nombre').text}")
    
    except ET.ParseError:
        print("Error al analizar el archivo XML.")

def modificar_stock(direccion_archivo, producto_id, nuevo_stock):
    try:
        arbol = ET.parse(direccion_archivo)
        raiz = arbol.getroot()

        print("Archivo XML cargado correctamente.")
        
        encontrado = False

        for producto in raiz.findall("productos"):
            if producto.get("id") == producto_id:
                producto.find("stock").text = str(nuevo_stock)
                arbol.write(direccion_archivo, encoding='utf-8', xml_declaration=True)
                print(f"Stock actualizado para el producto ID {producto_id}.")
                encontrado = True
                break 

        if not encontrado:
            print(f"Producto con ID {producto_id} no encontrado.")

    except ET.ParseError:
        print("Error al analizar el archivo XML.")

direccion_archivo = r"punto2/catalogo.xml"
mostrar_productos_disponibles(direccion_archivo)

producto_id = input("Ingresa el ID del producto que deseas modificar: ")
nuevo_stock = input("Ingresa el nuevo stock para el producto: ")

modificar_stock(direccion_archivo, producto_id, nuevo_stock)
