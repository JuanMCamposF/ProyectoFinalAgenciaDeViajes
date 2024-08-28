# Datos de vuelos entre ciudades
vuelos = {
    "1": {"ciudad": "Bogotá", "salidas": {"2": 50000, "3": 40000, "4": 60000}},
    "2": {"ciudad": "Cali", "salidas": {"1": 50000, "3": 30000, "4": 70000}},
    "3": {"ciudad": "Medellín", "salidas": {"1": 40000, "2": 30000, "4": 50000}},
    "4": {"ciudad": "Cartagena", "salidas": {"1": 60000, "2": 70000, "3": 50000}}
}

# Datos de hoteles en cada ciudad
hoteles = {"1": {
        "1": {"nombre": "Hotel JW Marriott Bogotá", "precio": 800000, "plan_turismo": "Visita al cerro de Monserrate, tour por la Candelaria y almuerzo en La Macarena"},
        "2": {"nombre": "Hotel W Bogotá", "precio": 600000, "plan_turismo": "Visita al Museo del Oro, tour por la zona T y cena en el restaurante Andrés DC"},
        "3": {"nombre": "Hotel Hilton Bogotá", "precio": 700000, "plan_turismo": "Visita al Parque 93, tour por la zona rosa y desayuno en el café San Alberto"}
    },
    "2": {
        "1": {"nombre": "Hotel InterContinental Cali", "precio": 500000, "plan_turismo": "Visita al valle del Cauca, tour por el centro histórico y cena en el restaurante El Cielo"},
        "2": {"nombre": "Hotel Now Cali", "precio": 400000, "plan_turismo": "Visita al Museo del Valle del Cauca, tour por el barrio San Antonio y desayuno en el café La Castilla"},
        "3": {"nombre": "Hotel Four Points by Sheraton Cali", "precio": 550000, "plan_turismo": "Visita al parque de la Caña, tour por el barrio Granada y almuerzo en el restaurante La Casa de las Ensaladas"}
    },
    "3": {
        "1": {"nombre": "Hotel Park 10", "precio": 450000, "plan_turismo": "Visita al parque Lleras, tour por el barrio El Poblado y cena en el restaurante El Cielo"},
        "2": {"nombre": "Hotel Poblado Alejandria", "precio": 350000, "plan_turismo": "Visita al Museo de Antioquia, tour por el centro histórico y desayuno en el café Velvet"},
        "3": {"nombre": "Hotel NH Medellín", "precio": 500000, "plan_turismo": "Visita al Jardín Botánico, tour por el barrio La Llanura y almuerzo en el restaurante La Casa de las Ensaladas"}
    },
    "4": {
        "1": {"nombre": "Hotel Sofitel Legend Santa Clara", "precio": 900000, "plan_turismo": "Visita al centro histórico, tour por la muralla y cena en el restaurante La Cevichería"},
        "2": {"nombre": "Hotel Casa San Agustín", "precio": 700000, "plan_turismo": "Visita al Castillo de San Felipe de Barajas, tour por el barrio Getsemaní y desayuno en el café San Alberto"},
        "3": {"nombre": "Hotel Hyatt Regency Cartagena", "precio": 800000, "plan_turismo": "Visita al mar Caribe, tour por el barrio Bocagrande y almuerzo en el restaurante La Casa de las Ensaladas"}
    }
}

# Función para formatear el precio con puntos como separadores de miles
def formatear_precio(precio):
    return "{:,}".format(precio).replace(",", ".")

# Lista para almacenar los pasajeros registrados
pasajeros = []

# Función para mostrar el menú de selección de ciudades
def mostrar_menu_ciudades():
    print("Seleccione una ciudad:")
    for clave, valor in vuelos.items():
        print(f"{clave}. {valor['ciudad']}")

# Función para seleccionar una ciudad de entre las opciones del menú
def seleccionar_ciudad(mensaje):
    mostrar_menu_ciudades()
    opcion = input(mensaje)
    if opcion in vuelos:
        return opcion
    else:
        print("Opción inválida. Inténtelo de nuevo.")
        return seleccionar_ciudad(mensaje)

# Función para seleccionar un plan de hotel en la ciudad elegida
def seleccionar_plan(ciudad):
    hoteles_ciudad = hoteles[ciudad]
    print(f"Hoteles en {vuelos[ciudad]['ciudad']}:")
    for i, (clave, info) in enumerate(hoteles_ciudad.items(), start=1):
        print(f"{i}. {info['nombre']}: ${formatear_precio(info['precio'])} COP, {info['plan_turismo']}")
    try:
        seleccion = int(input("Seleccione un hotel (1-3): "))
        if seleccion in range(1, 4):
            return hoteles_ciudad[str(seleccion)]
        else:
            print("Selección inválida.")
            return None
    except ValueError:
        print("Entrada inválida.")
        return None

# Función para seleccionar el vuelo y el tipo de viaje (ida o ida y vuelta)
def vuelo(salida, llegada):
    num_personas = int(input("Ingrese el número de personas: "))
    global pasajeros
    pasajeros = []
    # Recolecta datos de los pasajeros
    for i in range(num_personas):
        cedula = input(f"Ingrese el número de cédula del pasajero {i+1}: ")
        nombre = input(f"Ingrese el nombre del pasajero {i+1}: ")
        pasajeros.append({"cedula": cedula, "nombre": nombre})
    print("¿Desea un vuelo de ida y vuelta o solo ida?")
    print("1. Ida y vuelta")
    print("2. Solo ida")
    tipo_vuelo = input("Ingrese su opción: ")
    # Calcula el precio para vuelo de ida y vuelta
    if tipo_vuelo == "1":
        if salida in vuelos and llegada in vuelos[salida]["salidas"]:
            precio_ida = vuelos[salida]["salidas"][llegada] * num_personas
            precio_vuelta = vuelos[llegada]["salidas"][salida] * num_personas
            total_precio = precio_ida + precio_vuelta
            print(f"El vuelo de ida y vuelta de {vuelos[salida]['ciudad']} a {vuelos[llegada]['ciudad']} para {num_personas} personas cuesta ${formatear_precio(total_precio)}")
            return total_precio, num_personas
        else:
            print("No hay vuelos disponibles entre estas ciudades")
            return None, None
    # Calcula el precio para vuelo de solo ida
    elif tipo_vuelo == "2":
        if salida in vuelos and llegada in vuelos[salida]["salidas"]:
            precio_ida = vuelos[salida]["salidas"][llegada] * num_personas
            print(f"El vuelo de ida de {vuelos[salida]['ciudad']} a {vuelos[llegada]['ciudad']} para {num_personas} personas cuesta ${formatear_precio(precio_ida)}")
            return precio_ida, num_personas
        else:
            print("No hay vuelos disponibles entre estas ciudades")
            return None, None
    else:
        print("Opción inválida")
        return None, None

# Función para calcular el costo total del hotel seleccionado
def calcular_costo(plan, num_personas):
    return plan['precio'] * num_personas

# Función del menú principal de la agencia de viajes
def menu():
    print("Bienvenido a la Agencia de Viajes")
    print("1. Planificación de viaje")
    print("2. Registro de usuario")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        return "planificacion"
    elif opcion == "2":
        return "registro"
    elif opcion == "3":
        return "salir"
    else:
        print("Opción no válida, inténtelo de nuevo.")
        return menu()

# Base de datos simulada para almacenar los usuarios registrados
db = {}

# Función para agregar un usuario a la base de datos
def agregar_usuario(cedula, nombre):
    db[cedula] = {"nombre": nombre}
    print(f"Usuario agregado: {nombre} con cédula {cedula}")

# Función para verificar si un usuario ya está registrado
def verificar_usuario(cedula):
    if cedula in db:
        print(f"Usuario encontrado: {db[cedula]['nombre']} con cédula {cedula}")
        return True
    else:
        print("Usuario no encontrado. Por favor, regístrese.")
    return False

# Función para registrar un nuevo usuario
def registro_usuario():
    cedula = input("Ingrese su cédula: ")
    nombre = input("Ingrese su nombre: ")
    agregar_usuario(cedula, nombre)
    print("Registro completo. Por favor, ingrese nuevamente.")
    return cedula

# Función para el inicio del proceso de planificación del viaje
def iniciar_planificacion():
    while True:
        salida = seleccionar_ciudad("Seleccione la ciudad de salida: ")
        llegada = seleccionar_ciudad("Seleccione la ciudad de llegada: ")
        if salida != llegada:
            break
        else:
            print("La ciudad de salida y de llegada no pueden ser la misma. Inténtelo de nuevo.")

    total_precio, num_personas = vuelo(salida, llegada)
    if total_precio is not None:
        plan = seleccionar_plan(llegada)
        if plan is not None:
            costo_hotel = calcular_costo(plan, num_personas)
            print(f"El costo del hotel seleccionado es ${formatear_precio(costo_hotel)} COP")
            costo_total = total_precio + costo_hotel
            print(f"El costo total del viaje para {num_personas} personas es: ${formatear_precio(costo_total)} COP")

# Función principal para ejecutar el programa
def main():
    cedula = None
    while True:
        opcion = menu()
        if opcion == "registro":
            cedula = registro_usuario()
        elif opcion == "planificacion":
            if not cedula:
                cedula = input("Por favor, ingrese su cédula para continuar: ")
            if not verificar_usuario(cedula):
                print("Debe registrarse antes de planificar un viaje.")
                continue
            iniciar_planificacion()
        elif opcion == "salir":
            print("Gracias por usar nuestra agencia de viajes. ¡Hasta luego!")
            break
main()
