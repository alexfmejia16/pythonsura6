#los diccionaros son variables especiales que me permiten almacen multiples de datos 
#de diferete tipo en una sola variable.

empleado={
    'nombre':"juan",
    'cedula':10203056,
    'cargo':"Analista de datos",
    'Salario':8000000,
    'horasTrabajadas':40,
    'aplicaSubsidioTransporte':False,
    'deudas':[1500000,800000]

}
print(empleado)
print(empleado['deudas'][0])


#Recorriendo un diccionario:
for observadorAtributo,observadorValor in empleado.items():
    print(observadorAtributo)
    print(observadorValor)
