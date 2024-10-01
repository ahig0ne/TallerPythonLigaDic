import ligabet as lb

def verEquipo():
    if len(lb.ligaBetPlay) > 0:
            print('Equipos registrados:')
            for key, value in lb.ligaBetPlay.items():
                print(f'{key}: {value['nombre']}')
            
            numeroEquipo = input('Ingrese el número del equipo para ver detalles: ')
            
            equipoSeleccionado = lb.ligaBetPlay.get(numeroEquipo)
            
            if equipoSeleccionado:
                print(f'\nDetalles del equipo: {equipoSeleccionado['nombre']}')
                mostrarCuerpoTecnico(equipoSeleccionado)
            else:
                print('El equipo seleccionado no existe. Intente nuevamente.')
            
            input('Presione Enter para continuar...')
            lb.main.registrar()
    else:
        print('No hay equipos registrados en la liga.')
        input('Presione Enter para continuar...')
        lb.main.registrar()

def mostrarCuerpoTecnico(equipo):
    cuerpoTecnico = equipo.get('cuerpoTecnico', {})
    print('\nCuerpo Técnico:')
    if cuerpoTecnico:
        print(f'Director Técnico (DT): {cuerpoTecnico.get('tecnico', 'No registrado')}')
        print(f'Asistente Técnico (AT): {cuerpoTecnico.get('asistente', 'No registrado')}')
        print(f'Preparador Físico: {cuerpoTecnico.get('prepFisico', 'No registrado')}')
    else:
        print('No hay cuerpo técnico registrado.')

def mostrarEstadisticasEquipo(equipo):
    estadisticas = equipo['estadisticas']
    print(f'\nEstadísticas del equipo {equipo['nombre']}:')
    print(f'Partidos jugados : {estadisticas['PJ']}')
    print(f'Partidos ganados : {estadisticas['PG']}')
    print(f'Partidos perdidos : {estadisticas['PP']}')
    print(f'Partidos empatados : {estadisticas['PE']}')
    print(f'Goles a favor : {estadisticas['GF']}')
    print(f'Goles en contra : {estadisticas['GC']}')
    print(f'Puntos totales : {estadisticas['TP']}\n')
    print(f'Tarjetas rojas totales : {estadisticas['TR']}\n')
    print(f'Tarjetas amarillas totales : {estadisticas['TA']}\n')
    print(f'Tarjetas acumuladas en el equipo : {estadisticas['TT']}\n')
    enter=bool(input('Presione cualquier tecla para continuar.'))
    lb.main.programar()

def mostrarJugadoresEquipo(equipo):
    print(f'\nJugadores del equipo {equipo['nombre']}:')
    if equipo['jugadores']:
        for numero, jugador in equipo['jugadores'].items():
            print(f'Camisa {numero}: {jugador['nombre']} (Tarjetas Amarillas: {jugador['tarjetasAmarillas']}, Tarjetas Rojas: {jugador['tarjetasRojas']})')
    else:
        enter=bool(input('Este equipo no tiene jugadores registrados.'))

def menuSeleccionarEquipo():
    while True:
        print('\n===== Selección de equipo =====')
        # Mostrar los equipos disponibles
        for numero, equipo in lb.ligaBetPlay.items():
            print(f"{numero}: {equipo['nombre']}")
        
        numeroEquipo = input('Ingrese el número del equipo para ver sus jugadores o "s" para salir: ').strip()

        # Si el usuario quiere salir
        if numeroEquipo.lower() == 's':
            print('Saliendo del menú.')
            break

        # Verificar si se ingresó un número válido
        try:
            numeroEquipo = int(numeroEquipo)
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")
            continue

        # Obtener el equipo seleccionado
        equipoSeleccionado = lb.ligaBetPlay.get(numeroEquipo)

        if equipoSeleccionado:
            # Llamar a la función para mostrar los jugadores del equipo
            mostrarJugadoresEquipo(equipoSeleccionado)
        else:
            print('Equipo no encontrado. Intente nuevamente.')

def mostrarResultadosFinales():
    equipoGanador = None
    equipoMasTarjetas = None
    jugadorMasTarjetas = None
    maxPuntos = -1
    maxTarjetasEquipo = -1
    maxTarjetasJugador = -1

    for numeroEquipo, equipo in lb.ligaBetPlay.items():
        if equipo['estadisticas']['TP'] > maxPuntos:
            maxPuntos = equipo['estadisticas']['TP']
            equipoGanador = equipo['nombre']

        totalTarjetasEquipo = equipo['estadisticas']['TT']
        if totalTarjetasEquipo > maxTarjetasEquipo:
            maxTarjetasEquipo = totalTarjetasEquipo
            equipoMasTarjetas = equipo['nombre']

        for numeroJugador, jugador in equipo['jugadores'].items():
            totalTarjetasJugador = jugador['tarjetasAmarillas'] + jugador['tarjetasRojas']
            if totalTarjetasJugador > maxTarjetasJugador:
                maxTarjetasJugador = totalTarjetasJugador
                jugadorMasTarjetas = jugador['nombre']

    print('\n===== Resultados Finales =====')
    if equipoGanador:
        print(f'El equipo ganador es: {equipoGanador} con {maxPuntos} puntos.')
    if equipoMasTarjetas:
        print(f'El equipo con más tarjetas es: {equipoMasTarjetas} con {maxTarjetasEquipo} tarjetas.')
    if jugadorMasTarjetas:
        print(f'El jugador con más tarjetas es: {jugadorMasTarjetas} con {maxTarjetasJugador} tarjetas.')

    print('\nEl programa ha terminado. ¡Gracias por jugar!')
    exit()