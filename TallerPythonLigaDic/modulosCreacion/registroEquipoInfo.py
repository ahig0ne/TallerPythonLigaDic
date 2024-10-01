import ligabet as lb

def agregarJugadores():
    while True:
        print("\nEquipos disponibles:")
        for numero, equipo in lb.ligaBetPlay.items():
            print(f"{numero}: {equipo['nombre']}")
        
        numeroEquipo = input("Ingrese el número del equipo al que desea agregar un jugador: ")
        if numeroEquipo not in lb.ligaBetPlay:
            print("Equipo no encontrado. Intente de nuevo.")
            continue
        
        nombreJugador = input("Ingrese el nombre del jugador: ")
        
        while True:
            try:
                numeroJugador = int(input('Ingrese el número de la camisa del jugador: '))
                break
            except ValueError:
                print("Entrada no válida para el número de camisa. Debe ser un número. Intente de nuevo.")
        
        jugador = {
            'nombre': nombreJugador,
            'camisa': numeroJugador,
            'tarjetasAmarillas': 0,
            'tarjetasRojas': 0,
            'posicion': ''
        }

        print(lb.msg.msgPosicionJugador)
        
        while True:
            try:
                posicionJugador = int(input("Ingrese la posición del jugador (1-5): "))
                posiciones = {
                    1: 'Portero',
                    2: 'Defensa',
                    3: 'Lateral',
                    4: 'Medio Campo',
                    5: 'Delantero'
                }
                jugador['posicion'] = posiciones.get(posicionJugador, "Posición no válida")
                if jugador['posicion'] == "Posición no válida":
                    print(jugador['posicion'])
                    continue
                break
            except ValueError:
                print("Entrada no válida. Intente de nuevo. El valor debe ser un número entre 1 y 5.")
        
        lb.ligaBetPlay[numeroEquipo]['jugadores'][numeroJugador] = jugador
        print(f'El jugador {nombreJugador} con posicion {jugador['posicion']}se ha agregado al equipo {lb.ligaBetPlay[numeroEquipo]["nombre"]}.')
        
        while True:
            lb.os.system('cls')
            continuar = input("¿Desea agregar otro jugador? (s/n): ").strip().lower()
            if continuar in ['s', 'n']:
                break
            else:
                print("Entrada no válida.")
        if continuar == 'n':
            lb.sb.registrarEquipo()

def agregarCuerpoTecnico():
    while True:
        for numero, equipo in lb.ligaBetPlay.items():
            print(f"{numero}: {equipo['nombre']}")

        numeroEquipo = input("Ingrese el número del equipo al que desea agregar un cuerpo técnico: ")
        if numeroEquipo not in lb.ligaBetPlay:
            print("Equipo no encontrado. Intente de nuevo.")
            continue
        cuerpoTecnico = lb.ligaBetPlay[numeroEquipo].setdefault('cuerpoTecnico', {
            'tecnico': '',
            'asistente': '',
            'prepFisico': ''
        })
        if cuerpoTecnico['tecnico']:
            print("El equipo ya contiene un cuerpo técnico.")
            lb.sb.registrarEquipo()
        try:
            while True:
                nombredt = input('Ingrese nombre del director técnico: ').strip()
                if nombredt:
                    cuerpoTecnico['tecnico'] = nombredt
                    print(f'El director técnico {nombredt} se ha agregado correctamente al equipo {lb.ligaBetPlay[numeroEquipo]["nombre"]}.')
                    break
                else:
                    print("El nombre del director técnico no puede estar vacío. Intente de nuevo.")
            while True:
                nombreat = input('Ingrese nombre del asistente técnico: ').strip()
                if nombreat:
                    cuerpoTecnico['asistente'] = nombreat
                    print(f'El asistente técnico {nombreat} se ha agregado correctamente al equipo {lb.ligaBetPlay[numeroEquipo]["nombre"]}.')
                    break
                else:
                    print("El nombre del asistente técnico no puede estar vacío. Intente de nuevo.")
            
            while True:
                nombrePrep = input('Ingrese nombre del preparador físico: ').strip()
                if nombrePrep:
                    cuerpoTecnico['prepFisico'] = nombrePrep
                    print(f'El preparador físico {nombrePrep} se ha agregado correctamente al equipo {lb.ligaBetPlay[numeroEquipo]["nombre"]}.')
                    break
                else:
                    print("El nombre del preparador físico no puede estar vacío. Intente de nuevo.")

        except Exception as e:
            print(f"Error al agregar cuerpo técnico: {e}")
        while True:
            continuar = input("¿Desea agregar cuerpo técnico a otro equipo? (s/n): ").strip().lower()
            if continuar in ['s', 'n']:
                break
            else:
                print("Entrada no válida. Escriba 's' para sí o 'n' para no.")        
        if continuar == 'n':
            lb.sb.registrarEquipo()

def agregarCuerpoMedico():
    while True:
        try:
            print("\nEquipos disponibles:")
            for numero, equipo in lb.ligaBetPlay.items():
                print(f"{numero}: {equipo['nombre']}")
            
            numeroEquipo = input("Ingrese el número del equipo al que desea agregar un cuerpo médico: ")
            if numeroEquipo not in lb.ligaBetPlay:
                raise ValueError("Equipo no encontrado. Intente de nuevo.")
            
            cuerpoMedico = lb.ligaBetPlay[numeroEquipo].setdefault('cuerpoMedico', {
                'medico': '',
            })
            if cuerpoMedico['medico']:
                print(f"El equipo {lb.ligaBetPlay[numeroEquipo]['nombre']} ya tiene un médico asignado.")
                return
            while True:
                try:
                    nombreCuerpomedico = input('Ingrese nombre del médico: ').strip()
                    if not nombreCuerpomedico:
                        raise ValueError("El nombre del médico no puede estar vacío. Intente de nuevo.")
                    cuerpoMedico['medico'] = nombreCuerpomedico
                    print(f'El médico {nombreCuerpomedico} se ha agregado correctamente al equipo {lb.ligaBetPlay[numeroEquipo]["nombre"]}.')
                    break
                except ValueError as e:
                    print(e)

        except ValueError as e:
            print(e)
            continue
        
        try:
            while True:
                continuar = input("¿Desea agregar cuerpo médico a otro equipo? (s/n): ").strip().lower()
                if continuar not in ['s', 'n']:
                    raise ValueError("Entrada no válida. Escriba 's' para sí o 'n' para no.")
                break
        except ValueError as e:
            print(e)

        if continuar == 'n':
            lb.sb.registrarEquipo()



    