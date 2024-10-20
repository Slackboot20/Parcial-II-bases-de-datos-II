import json

def generar_json(direccion_archivo, datos):
    try:
        with open(direccion_archivo, 'a', encoding='utf-8') as archivo_json:
            json.dump(datos, archivo_json, indent=4, ensure_ascii=False)
        print(f"El archivo JSON fue creado con éxito.")
    except Exception as e:
        print(f"Ocurrió un error al crear el archivo JSON: {e}")

def ingresar_datos():
    datos = {}

    ciudad = str(input("Ingrese el ciudad encuestada: "))
    personas_encuestadas = int(input("Ingrese cuantas personas fueron encuestadas: "))
    transporte_utilizado=[]
    while True:
        transporte = str(input("ingrese un vehiculo o presione enter para terminar: "))

        if transporte:
            cantidad = int(input(f"cuantas personas escogieron {transporte}: "))
            transporte_utilizado.append({"transporte": transporte, "cantidad": cantidad})
        else:
            break
    
    datos["ciudad"] = ciudad
    datos["personas_encuestadas"] = personas_encuestadas
    datos["transporte_utilizado"] = transporte_utilizado

    return datos

direccion_json = r"C:\Users\Camil\OneDrive\Escritorio\Bases de datos II\Parcial II\Punto3\Encuestas.json"

datos_ingresados = ingresar_datos()
generar_json(direccion_json, datos_ingresados)