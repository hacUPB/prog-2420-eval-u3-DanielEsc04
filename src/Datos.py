import datetime

entrenamientos = {}

def planificar_entrenamiento(dia, tipo, duracion, distancia): #Funcion para planificar entrenamientos
    fecha_actual = datetime.date.today() 
    if dia >= fecha_actual: #Revisar si la fecha es igual o posterior a la actual
        if dia not in entrenamientos:
            entrenamientos[dia] = {"tipo": tipo, "duracion": duracion, "distancia": distancia}
            print(f"Entrenamiento planificado para {dia}: {tipo}, {duracion} minutos, {distancia} km")
        else:
            print(f"Ya existe un entrenamiento planificado para el día {dia}")
    else:
        print(f"No se puede planificar un entrenamiento para una fecha pasada ({dia}). Debe ser igual o posterior a {fecha_actual}.")

def registrar_entrenamiento(dia, tipo, duracion, distancia): #Funcion para registrar un entrenamiento pasado
    fecha_actual = datetime.date.today()
    if dia <= fecha_actual: #Revisar si la fecha es igual o anterior a la actual
        if dia in entrenamientos:
            entrenamientos[dia]["tipo"] = tipo
            entrenamientos[dia]["duracion"] = duracion
            entrenamientos[dia]["distancia"] = distancia
            print(f"Entrenamiento registrado para {dia}: {tipo}, {duracion} minutos, {distancia} km")
        else:
            print(f"No hay entrenamiento registrado para el día {dia}")
    else:
        print(f"No se puede registrar un entrenamiento para una fecha futura ({dia}). Debe ser igual o anterior a {fecha_actual}.")

def consultar_progreso(): #Función para revisar el progreso
    if entrenamientos:
        for dia in entrenamientos:
            print(f"Fecha: {dia} // Tipo: {entrenamientos[dia]['tipo']} // Duración: {entrenamientos[dia]['duracion']} minutos // Distancia: {entrenamientos[dia]['distancia']} km")
    else:
        print("No hay entrenamientos planificados.")

def validar_fecha(fecha_str): #Funcion para convertir fecha de str a date
    try:
        fecha = datetime.datetime.strptime(fecha_str, "%Y-%m-%d").date() 
        return fecha
    except ValueError:
        print("Fecha no válida. Debe tener el formato YYYY-MM-DD.")
        return None

def UI(): #Menu
    while True:
        opcion = int(input("Qué desea realizar?\n1) Planificar entrenamiento\n2) Registrar entrenamiento\n3) Consultar progreso\n4) Salir\n"))
        
        if opcion == 1:
            dia = None
            while dia is None:
                dia = validar_fecha(input("Ingrese el día del entrenamiento (formato YYYY-MM-DD): "))
            
            tipo = None
            while tipo is None:
                tipo_opcion = int(input("Ingrese el tipo de entrenamiento:\n1) Natación\n2) Ciclismo\n3) Running\n4) Gym\n"))
                if tipo_opcion == 1:
                    tipo = "Natación"
                elif tipo_opcion == 2:
                    tipo = "Ciclismo"
                elif tipo_opcion == 3:
                    tipo = "Running"
                elif tipo_opcion == 4:
                    tipo = "Gym"
                else:
                    print("Ingrese un tipo de entrenamiento adecuado.")
            
            duracion = int(input("Ingrese la duración en minutos: "))
            distancia = float(input("Ingrese la distancia en kilómetros: "))
            planificar_entrenamiento(dia, tipo, duracion, distancia)
            
        elif opcion == 2:
            dia = None
            while dia is None:
                dia = validar_fecha(input("Ingrese el día del entrenamiento (formato YYYY-MM-DD): "))
            
            tipo = None
            while tipo is None:
                tipo_opcion = int(input("Ingrese el tipo de entrenamiento:\n1) Natación\n2) Ciclismo\n3) Running\n4) Gym\n"))
                if tipo_opcion == 1:
                    tipo = "Natación"
                elif tipo_opcion == 2:
                    tipo = "Ciclismo"
                elif tipo_opcion == 3:
                    tipo = "Running"
                elif tipo_opcion == 4:
                    tipo = "Gym"
                else:
                    print("Ingrese un tipo de entrenamiento adecuado.")
            
            duracion = int(input("Ingrese la duración en minutos: "))
            distancia = float(input("Ingrese la distancia en kilómetros: "))
            registrar_entrenamiento(dia, tipo, duracion, distancia)
            
        elif opcion == 3:
            consultar_progreso()
            
        elif opcion == 4:
            print("Saliendo del programa...")
            break
            
        else:
            print("Ingrese una opción válida")

if __name__ == "__main__":
    UI()
