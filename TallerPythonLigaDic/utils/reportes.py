import ligabet as lb

def resultadoPartido():
    lb.os.system('cls')
    for numero, equipo in lb.ligaBetPlay.items():
        print(f'{numero}: {equipo['nombre']}')

    equipoLocal = input('Ingresa el nombre del Local: ')
    equipoVisit = input('Ingresa el nombre del visitante: ')
    
    try:
        golesEquipoLocal = int(input(f'Ingrese los goles de {equipoLocal}: '))
        golesEquipoVisit = int(input(f'Ingrese los goles de {equipoVisit}: '))
    except ValueError:
        print('Entrada no válida. Los goles deben ser números enteros.')
        resultadoPartido()
    
    equipoLocalEncontrado = None
    equipoVisitEncontrado = None

    for numero, equipo in lb.ligaBetPlay.items():
        if equipo['nombre'] == equipoLocal:
            equipoLocalEncontrado = equipo
        if equipo['nombre'] == equipoVisit:
            equipoVisitEncontrado = equipo

    if not equipoLocalEncontrado:
        print(f'El equipo {equipoLocal} no existe en la liga.')
        resultadoPartido()
    if not equipoVisitEncontrado:
        print(f'El equipo {equipoVisit} no existe en la liga.')
        resultadoPartido()

    equipoLocalEncontrado['estadisticas']['PJ'] += 1
    equipoLocalEncontrado['estadisticas']['GF'] += golesEquipoLocal
    equipoLocalEncontrado['estadisticas']['GC'] += golesEquipoVisit

    equipoVisitEncontrado['estadisticas']['PJ'] += 1
    equipoVisitEncontrado['estadisticas']['GF'] += golesEquipoVisit
    equipoVisitEncontrado['estadisticas']['GC'] += golesEquipoLocal

    if golesEquipoLocal > golesEquipoVisit:
        equipoLocalEncontrado['estadisticas']['PG'] += 1
        equipoLocalEncontrado['estadisticas']['TP'] += 3
        equipoVisitEncontrado['estadisticas']['PP'] += 1
        lb.main.menuPrincipal()

    elif golesEquipoLocal == golesEquipoVisit:
        equipoLocalEncontrado['estadisticas']['PE'] += 1
        equipoLocalEncontrado['estadisticas']['TP'] += 1
        equipoVisitEncontrado['estadisticas']['PE'] += 1
        equipoVisitEncontrado['estadisticas']['TP'] += 1
        lb.main.menuPrincipal()
    else:
        equipoLocalEncontrado['estadisticas']['PP'] += 1
        equipoVisitEncontrado['estadisticas']['PG'] += 1
        equipoVisitEncontrado['estadisticas']['TP'] += 3
        lb.main.menuPrincipal()

    resultadoPartido()


def reportarTarjetas(jugador, equipo):
    while True:
        try:
            print(f'\nReportando tarjetas para {jugador['nombre']}:')
            opcion = input('Ingrese "a" para agregar una tarjeta amarilla, "r" para agregar una tarjeta roja, o "s" para salir: ').strip().lower()

            if opcion == 'a':
                jugador['tarjetasAmarillas'] += 1
                equipo['estadisticas']['tarjetasAmarillasTotales'] += 1
                equipo['estadisticas']['tarjetasTotales'] += 1
                print(f'Tarjeta amarilla agregada a {jugador['nombre']}. Total: {jugador['tarjetasAmarillas']}.')
                print(f'Tarjetas amarillas totales del equipo: {equipo['estadisticas']['tarjetasAmarillasTotales']}.')
            elif opcion == 'r':
                jugador['tarjetasRojas'] += 1
                equipo['estadisticas']['tarjetasRojasTotales'] += 1
                equipo['estadisticas']['tarjetasTotales'] += 1
                print(f'Tarjeta roja agregada a {jugador['nombre']}. Total: {jugador['tarjetasRojas']}.')
                print(f'Tarjetas rojas totales del equipo: {equipo['estadisticas']['tarjetasRojasTotales']}.')
            elif opcion == 's':
                print('Saliendo del reporte de tarjetas.')
                lb.sb.menuJugadores()
            else:
                print('Opción no válida. Intente de nuevo.')
        except Exception as e:
            print(f'Error al reportar tarjeta: {e}')

def menuReportarTarjetas():
    while True:
        print('\nEquipos disponibles:')
        # Mostrar los equipos disponibles
        for equipo in lb.ligaBetPlay.values():
            print(f"- {equipo['nombre']}")  # Se imprime el nombre del equipo

        # Solicitar la entrada del usuario
        equipoSeleccionadoNombre = input('Ingrese el nombre del equipo para ver sus jugadores o "s" para salir: ').strip()

        # Verificar si el usuario quiere salir
        if equipoSeleccionadoNombre.lower() == 's':
            print('Saliendo del menú de reportar tarjetas.')
            break

        # Buscar el equipo por nombre
        equipoSeleccionado = next((equipo for equipo in lb.ligaBetPlay.values() if equipo['nombre'].lower() == equipoSeleccionadoNombre.lower()), None)

        if equipoSeleccionado:
            lb.vw.mostrarJugadoresEquipo(equipoSeleccionado)

            # Verificar si el equipo tiene jugadores
            if equipoSeleccionado.get('jugadores'):
                numeroJugador = input('Ingrese el número de la camisa del jugador para reportar tarjetas o "s" para salir: ').strip()
                if numeroJugador.lower() == 's':
                    continue

                # Intentar convertir el número de la camisa a entero
                try:
                    numeroJugador = int(numeroJugador)

                    # Obtener el jugador seleccionado
                    jugadorSeleccionado = equipoSeleccionado['jugadores'].get(numeroJugador)

                    if jugadorSeleccionado:
                        reportarTarjetas(jugadorSeleccionado, equipoSeleccionado)
                    else:
                        print('Jugador no encontrado. Intente nuevamente.')
                except ValueError:
                    print('El número de la camisa debe ser un número válido.')
            else:
                print('El equipo no tiene jugadores registrados.')
        else:
            print('Equipo no encontrado. Intente nuevamente.')


def menuResultados():
    while True:
        print('\n===== Menú de Resultados =====')
        print('1. Ver resultados finales')
        print('2. Salir')
        opcion = input('Seleccione una opción: ').strip()

        if opcion == '1':
            lb.vw.mostrarResultadosFinales()
        elif opcion == '2':
            print('Saliendo del programa...')
            exit()
        else:
            print('Opción no válida, por favor intente de nuevo.')