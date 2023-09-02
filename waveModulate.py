import numpy as np
import matplotlib.pyplot as plt

# Función para la modulación ASK
def ask_modulation(cadena_binaria, duracion_bit, amplitud_alta, amplitud_baja, frecuencia_total, rango_forma):
    tiempo = np.arange(0, len(cadena_binaria) * duracion_bit, 1 / rango_forma)
    onda_portadora = np.sin(2 * np.pi * frecuencia_total * tiempo)
    senal_modulada = np.zeros(len(tiempo))

    for i, bit in enumerate(cadena_binaria):
        valor_bit = int(bit)
        if valor_bit == 0:
            senal = amplitud_baja * onda_portadora[i * int(duracion_bit * rango_forma):(i + 1) * int(duracion_bit * rango_forma)] + 0.10
        else:
            senal = amplitud_alta * onda_portadora[i * int(duracion_bit * rango_forma):(i + 1) * int(duracion_bit * rango_forma)]
        senal_modulada[i * int(duracion_bit * rango_forma):(i + 1) * int(duracion_bit * rango_forma)] = senal

    return tiempo, senal_modulada

# Función para la modulación FSK
def fsk_modulation(cadena_binaria, duracion_bit, frecuencia_0, frecuencia_1, amplitud, rango_forma):
    tiempo = np.arange(0, len(cadena_binaria) * duracion_bit, 1 / rango_forma)
    senal_modulada = np.zeros(len(tiempo))

    for i, bit in enumerate(cadena_binaria):
        valor_bit = int(bit)
        if valor_bit == 0:
            senal = amplitud * np.sin(2 * np.pi * frecuencia_0 * np.arange(0, duracion_bit, 1 / rango_forma))
        else:
            senal = amplitud * np.sin(2 * np.pi * frecuencia_1 * np.arange(0, duracion_bit, 1 / rango_forma))
        senal_modulada[i * int(duracion_bit * rango_forma):(i + 1) * int(duracion_bit * rango_forma)] = senal

    return tiempo, senal_modulada

# Función para la modulación PSK-2
def psk2_modulation(cadena_binaria, duracion_bit, frecuencia_portadora, amplitud, rango_forma):
    tiempo = np.arange(0, len(cadena_binaria) * duracion_bit, 1 / rango_forma)
    senal_modulada = np.zeros(len(tiempo))

    # Mapeo de fase para PSK-2
    mapeo_fase = {
        '0': 0,         # Ángulo de fase para el bit '0' es 0 grados (0 radianes)
        '1': np.pi      # Ángulo de fase para el bit '1' es π radianes (180 grados)
    }


    for i, bit in enumerate(cadena_binaria):
        fase = mapeo_fase[bit]
        senal = amplitud * np.sin(2 * np.pi * frecuencia_portadora * tiempo[i * int(duracion_bit * rango_forma):(i + 1) * int(duracion_bit * rango_forma)] + fase)
        senal_modulada[i * int(duracion_bit * rango_forma):(i + 1) * int(duracion_bit * rango_forma)] = senal

    return tiempo, senal_modulada

# Función para la modulación PSK-4
def psk4_modulation(cadena_binaria, duracion_bit, frecuencia_portadora, amplitud, rango_forma):
    while True:
        tiempo = np.arange(0, len(cadena_binaria) * duracion_bit, 1 / rango_forma)
        senal_modulada = np.zeros(len(tiempo))

        # Mapeo de fase ajustado
        mapeo_fase = {
            '00': np.pi/4,   # Cambiado a 45 grados
            '01': 3*np.pi/4,  # Cambiado a 135 grados
            '10': 5*np.pi/4,  # Cambiado a 225 grados
            '11': 7*np.pi/4   # Cambiado a 315 grados
        }

        # Validar que la cadena_binaria tenga una longitud par
        if len(cadena_binaria) % 2 != 0:
            print("La cadena binaria debe tener una longitud par.")
            cadena_binaria = input("Ingresa una cadena de 0s y 1s (longitud par): ")
            continue

        # Validar que la cadena_binaria solo contenga combinaciones válidas de dos bits
        for i in range(0, len(cadena_binaria), 2):
            dibit = cadena_binaria[i:i+2]
            if dibit not in mapeo_fase:
                print(f"Combinación de bits inválida: {dibit}")
                cadena_binaria = input("Ingresa una cadena de 0s y 1s (combinaciones válidas de 2 bits): ")
                continue

        for i in range(0, len(cadena_binaria), 2):
            dibit = cadena_binaria[i:i+2]
            fase = mapeo_fase[dibit]
            senal = amplitud * np.sin(2 * np.pi * frecuencia_portadora * tiempo[i * int(duracion_bit * rango_forma):(i + 1) * int(duracion_bit * rango_forma)] + fase)
            senal_modulada[i * int(duracion_bit * rango_forma):(i + 1) * int(duracion_bit * rango_forma)] = senal

        return tiempo, senal_modulada





# Función para la modulación PSK-8
def psk8_modulation(cadena_binaria, duracion_bit, frecuencia_portadora, amplitud, rango_forma):
    while True:
        tiempo = np.arange(0, len(cadena_binaria) * duracion_bit, 1 / rango_forma)
        senal_modulada = np.zeros(len(tiempo))

       # Mapeo de fase para PSK-8
        mapeo_fase = {
            '000': 0,                # Ángulo de fase para '000' es 0 grados (0 radianes)
            '001': np.pi / 4,        # Ángulo de fase para '001' es π/4 radianes (45 grados)
            '010': np.pi / 2,        # Ángulo de fase para '010' es π/2 radianes (90 grados)
            '011': 3 * np.pi / 4,    # Ángulo de fase para '011' es 3π/4 radianes (135 grados)
            '100': np.pi,            # Ángulo de fase para '100' es π radianes (180 grados)
            '101': -3 * np.pi / 4,   # Ángulo de fase para '101' es -3π/4 radianes (-135 grados)
            '110': -np.pi / 2,       # Ángulo de fase para '110' es -π/2 radianes (-90 grados)
            '111': -np.pi / 4        # Ángulo de fase para '111' es -π/4 radianes (-45 grados)
        }

        # Validar que la cadena_binaria solo contenga combinaciones válidas de tres bits
        if len(cadena_binaria) % 3 != 0:
            print("La cadena binaria debe tener una longitud múltiplo de 3.")
            cadena_binaria = input("Ingresa una cadena de 0s y 1s (longitud múltiplo de 3): ")
            continue

        # Validar que la cadena_binaria solo contenga combinaciones válidas de tres bits
        for i in range(0, len(cadena_binaria), 3):
            tribit = cadena_binaria[i:i+3]
            if tribit not in mapeo_fase:
                print(f"Combinación de bits inválida: {tribit}")
                cadena_binaria = input("Ingresa una cadena de 0s y 1s (combinaciones válidas de 3 bits): ")
                continue

        for i in range(0, len(cadena_binaria), 3):
            tribit = cadena_binaria[i:i+3]
            fase = mapeo_fase[tribit]
            senal = amplitud * np.sin(2 * np.pi * frecuencia_portadora * tiempo[i * int(duracion_bit * rango_forma):(i + 1) * int(duracion_bit * rango_forma)] + fase)
            senal_modulada[i * int(duracion_bit * rango_forma):(i + 1) * int(duracion_bit * rango_forma)] = senal

        return tiempo, senal_modulada


# Función para la modulación QAM-4
def qam4_modulation(cadena_binaria, duracion_bit, frecuencia_portadora, amplitud, rango_forma):
    while True:
        tiempo = np.arange(0, len(cadena_binaria) * duracion_bit, 1 / rango_forma)
        senal_modulada = np.zeros(len(tiempo))

        # Mapeo de amplitud para QAM-4
        mapeo = {
            '00': complex(amplitud, amplitud),       # Complejo con parte real y parte imaginaria positivas
            '01': complex(-amplitud, amplitud),      # Complejo con parte real negativa y parte imaginaria positiva
            '10': complex(amplitud, -amplitud),      # Complejo con parte real positiva y parte imaginaria negativa
            '11': complex(-amplitud, -amplitud)      # Complejo con parte real y parte imaginaria negativas
        }

        # Validar que la cadena_binaria tenga una longitud múltiplo de 2
        if len(cadena_binaria) % 2 != 0:
            print("La cadena binaria debe tener una longitud múltiplo de 2.")
            cadena_binaria = input("Ingresa una cadena de 0s y 1s (longitud múltiplo de 2): ")
            continue

        # Validar que la cadena_binaria solo contenga combinaciones válidas de dos bits
        for i in range(0, len(cadena_binaria), 2):
            dibit = cadena_binaria[i:i+2]
            if dibit not in mapeo:
                print(f"Combinación de bits inválida: {dibit}")
                cadena_binaria = input("Ingresa una cadena de 0s y 1s (combinaciones válidas de 2 bits): ")
                continue

        for i in range(0, len(cadena_binaria), 2):
            dibit = cadena_binaria[i:i+2]
            simbolo = mapeo[dibit]
            senal_real = np.real(simbolo) * np.cos(2 * np.pi * frecuencia_portadora * tiempo[i * int(duracion_bit * rango_forma):(i + 1) * int(duracion_bit * rango_forma)]) + \
                         np.imag(simbolo) * np.sin(2 * np.pi * frecuencia_portadora * tiempo[i * int(duracion_bit * rango_forma):(i + 1) * int(duracion_bit * rango_forma)])
            senal_modulada[i * int(duracion_bit * rango_forma):(i + 1) * int(duracion_bit * rango_forma)] = senal_real

        return tiempo, senal_modulada


# Función para la modulación QAM-8
def qam8_modulation(cadena_binaria, duracion_bit, frecuencia_portadora, amplitud, rango_forma):
    while True:
        tiempo = np.arange(0, len(cadena_binaria) * duracion_bit, 1 / rango_forma)
        senal_modulada = np.zeros(len(tiempo))

        mapeo_fase = {
            '000': 0,               # 0 grados
            '001': np.pi / 4,       # 45 grados
            '010': np.pi / 2,       # 90 grados
            '011': 3 * np.pi / 4,   # 135 grados
            '100': np.pi,           #  180 grados
            '101': 5 * np.pi / 4,   # 225 grados
            '110': 3 * np.pi / 2,   # 270 grados
            '111': 7 * np.pi / 4    # 315 grados
        }

        mapeo_amplitud = {
            '101': amplitud,
            '011': amplitud,
            '001': amplitud,
            '111': amplitud,
            '100': amplitud / 2,
            '010': amplitud / 2,
            '000': amplitud / 2,
            '100': amplitud / 2
        }

        # Validar que la cadena_binaria solo contenga combinaciones válidas de tres bits
        if len(cadena_binaria) % 3 != 0:
            print("La cadena binaria debe tener una longitud múltiplo de 3.")
            cadena_binaria = input("Ingresa una cadena de 0s y 1s (longitud múltiplo de 3): ")
            continue

        for i in range(0, len(cadena_binaria), 3):
            tribit = cadena_binaria[i:i + 3]
            if tribit not in mapeo_fase:
                print(f"Combinación de bits inválida: {tribit}")
                cadena_binaria = input("Ingresa una cadena de 0s y 1s (combinaciones válidas de 3 bits): ")
                break
        else:
            break

    for i in range(0, len(cadena_binaria), 3):
        tribit = cadena_binaria[i:i + 3]
        fase = mapeo_fase[tribit]
        amplitud_actual = mapeo_amplitud[tribit]
        senal = amplitud_actual * np.sin(2 * np.pi * frecuencia_portadora * tiempo[i * int(duracion_bit * rango_forma):(i + 1) * int(duracion_bit * rango_forma)] + fase)
        senal_modulada[i * int(duracion_bit * rango_forma):(i + 1) * int(duracion_bit * rango_forma)] = senal

    return tiempo, senal_modulada




# Función para graficar una técnica de modulación
def graficar_modulacion(tiempo, senal_modulada, titulo, etiqueta_y, texto_y, amplitud, ticks_bits=None, etiquetas_bits=None, color_bit_1='b'):
    plt.plot(tiempo, senal_modulada, color_bit_1)  # Usar el color especificado para el bit 1
    plt.ylim(-amplitud, amplitud)
    plt.axhline(y=0, color='k', linestyle='-')
    plt.title(titulo)
    plt.xlabel("Tiempo (s)")
    plt.ylabel(etiqueta_y)
    plt.grid()
    if ticks_bits and etiquetas_bits:
        for tick, etiqueta in zip(ticks_bits, etiquetas_bits):
            plt.axvline(x=tick, color='r', linestyle='--')
    plt.legend(['Señal Modulada (Bit 1 en {})'.format(color_bit_1)])

# Bucle para permitir al usuario elegir la técnica de modulación y los parámetros
while True:
    print("""
                            ░█░█░█▀█░█░█░█▀▀░░░░░█▄█░█▀█░█▀▄░█░█░█░░░█▀█░▀█▀░█▀█░█▀▄
                            ░█▄█░█▀█░▀▄▀░█▀▀░▄▄▄░█░█░█░█░█░█░█░█░█░░░█▀█░░█░░█░█░█▀▄
                            ░▀░▀░▀░▀░░▀░░▀▀▀░░░░░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀
                                            (c) MikeDEV 2023 v1.0.6
    """)
    print("\n\n")

    # Menú interactivo
    print("Seleccione la técnica de modulación que desea utilizar:")
    print("1. ASK")
    print("2. FSK")
    print("3. 2-PSK")
    print("4. 4-PSK")
    print("5. 8-PSK")
    print("6. 4-QAM")
    print("7. 8-QAM")
    print("8. Salir")

    # Obtener la elección del usuario
    opcion = int(input("Ingrese el número de la técnica de modulación deseada (o 8 para salir): "))

    if opcion == 8:
        break  # Salir del bucle si el usuario selecciona la opción 8 (Salir)

    # Obtener la entrada del usuario
    cadena_binaria = input("Ingresa una cadena de 0s y 1s: ")
    duracion_bit = float(input("Ingresa la duración de cada bit en segundos: "))
    frecuencia_portadora = float(input("Ingresa la frecuencia de la portadora en Hz: "))

    if opcion != 1:  # Preguntar la amplitud solo si no se selecciona ASK
        amplitud = float(input("Ingresa la amplitud de la señal modulada: "))
    else:
        amplitud = 2  # Valor predeterminado de amplitud para ASK

    rango_forma = 1000

    # Validar que la cadena binaria sea válida según la técnica de modulación seleccionada
    if opcion == 4 or opcion == 6:
        if len(cadena_binaria) % 2 != 0:
            print("\n La cadena binaria debe tener una longitud par para 4-PSK y 4-QAM. \n")
            continue
        valid_chars = set("01")
        if not set(cadena_binaria).issubset(valid_chars):
            print("La cadena binaria solo puede contener 0s y 1s.")
            continue
    elif opcion == 7 or opcion == 5:
        if len(cadena_binaria) % 3 != 0:
            print("La cadena binaria debe tener una longitud múltiplo de 3 para 8-PSK Y 8-QAM.")
            continue
        valid_chars = set("01")
        if not set(cadena_binaria).issubset(valid_chars):
            print("La cadena binaria solo puede contener 0s y 1s.")
            continue

    



    # Generar señales moduladas según la elección del usuario
    if opcion == 1:
        tiempo, senal_modulada = ask_modulation(cadena_binaria, duracion_bit, 2, 1, frecuencia_portadora, rango_forma)
        titulo = "Modulación ASK"
    
    elif opcion == 2:
        tiempo, senal_modulada = fsk_modulation(cadena_binaria, duracion_bit, 2, 4, amplitud, rango_forma)
        titulo = "Modulación FSK"
    
    elif opcion == 3:
        tiempo, senal_modulada = psk2_modulation(cadena_binaria, duracion_bit, frecuencia_portadora, amplitud, rango_forma)
        titulo = "Modulación 2-PSK"
    
    elif opcion == 4:
        tiempo, senal_modulada = psk4_modulation(cadena_binaria, duracion_bit, frecuencia_portadora, amplitud, rango_forma)
        titulo = "Modulación 4-PSK"
    
    elif opcion == 5:
        tiempo, senal_modulada = psk8_modulation(cadena_binaria, duracion_bit, frecuencia_portadora, amplitud, rango_forma)
        titulo = "Modulación 8-PSK"
    
    elif opcion == 6:
        tiempo, senal_modulada = qam4_modulation(cadena_binaria, duracion_bit, frecuencia_portadora, amplitud, rango_forma)
        titulo = "Modulación 4-QAM"
    
    elif opcion == 7:
        tiempo, senal_modulada = qam8_modulation(cadena_binaria, duracion_bit, frecuencia_portadora, amplitud, rango_forma)
        titulo = "Modulación 8-QAM"
    
    else:
        print("Opción no válida. Por favor, seleccione una técnica de modulación válida.")

    # Mostrar la señal modulada
    if opcion in range(1, 8):
        ticks_bits = [i * duracion_bit for i in range(len(cadena_binaria))]
        graficar_modulacion(tiempo, senal_modulada, titulo, "Amplitud", amplitud + 0.4, amplitud, ticks_bits=ticks_bits, etiquetas_bits=cadena_binaria, color_bit_1='g')
        plt.show()
