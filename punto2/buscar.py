import json

def buscar_producto_en_json(direccion_json):

    with open(direccion_json, 'r', encoding='utf-8') as archivo_json:
        productos = json.load(archivo_json)

    print("IDs disponibles en el catálogo:")
    for producto in productos:
        print(f"- ID: {producto['id']}, Nombre: {producto['nombre']}")

    producto_id = input("\nIngresa el ID que quieres buscar: ")

    encontrado = False

    for producto in productos:
        if producto["id"] == producto_id:
            print(f"\nProducto encontrado: {json.dumps(producto, indent=4, ensure_ascii=False)}")
            encontrado = True
            break

    if not encontrado:
        print(f"\nProducto con ID {producto_id} no encontrado")

direccion_json = r"punto2/catalogo.json"
buscar_producto_en_json(direccion_json)
