import xmlschema

xsd_schema = xmlschema.XMLSchema('punto4/empleados.xsd')

if xsd_schema.is_valid('punto4/empleados1.xml'):
    print("El archivo XML es valido segun el esquema XSD.")
else:
    print("El archivo XML no es valido segun el esquema XSD.")
