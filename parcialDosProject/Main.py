import string

print("Bienvenido al sistema de bonificaciones")

#Ingresar los datos del usuario
salario_base = int(input("Ingrese su salario mensual: "))
cargo = str(input("Ingrese su cargo: "))
desempeño = str(input("Ingrese el nivel de su desempeño: "))


#Funcion para calcular las bonificaciones para directivo
def calcular_bonificacion_directivo(salario_base, desempeño):
    if desempeño == "alto":
        return salario_base * 0.20
    elif desempeño == "medio":
        return salario_base * 0.10
    else:
        return 0

#Funcion para calcular las bonificaciones para operativo
def calcular_bonificacion_operativo(salario_base, desempeño):
    if desempeño == "alto":
        return salario_base * 0.15
    elif desempeño == "medio":
        return salario_base * 0.05
    else:
        return 0

#Funcion para calcular el total
def calcular_total(salario_base, bonificacion):
    return salario_base + bonificacion


#Funcion para calcular bonificacion
def calcular_bonificacion(salario_base, cargo, desempeño):
    if cargo == "directivo":
        bonificacion = calcular_bonificacion_directivo(salario_base, desempeño)
    elif cargo == "operativo":
        bonificacion = calcular_bonificacion_operativo(salario_base, desempeño)
    else:
        bonificacion = 0

    total_a_recibir = calcular_total(salario_base, bonificacion)
    return (f"---Resumen del Pago---\n"
            f"Cargo: {str.capitalize(cargo)}\n"
            f"Nivel de Desempeño: {str.capitalize(desempeño)}\n"
            f"Salario Base: ${salario_base}\n"
            f"Bonificacion: ${bonificacion}\n"
            f"Total a recibir: ${total_a_recibir}")



#Probar las salidas
print(calcular_bonificacion(salario_base,cargo,desempeño))