import ligabet as lb

def menuEstadisticas():
    while True:
        for numero, equipo in lb.ligaBetPlay.items():
            print(f'{numero}: {equipo['nombre']}')
        
        numeroEquipo = input('Ingrese el número del equipo para ver sus estadísticas o "s" para salir: ').strip()
        
        if numeroEquipo.lower() == 's':
            enter=bool(input('Saliendo del menú de estadísticas.'))
            lb.main.programar()

        equipoSeleccionado = lb.ligaBetPlay.get(numeroEquipo)

        if equipoSeleccionado:
            lb.vw.mostrarEstadisticasEquipo(equipoSeleccionado)
        else:
            enter=bool(input('Equipo no encontrado. Intente nuevamente.'))
            menuEstadisticas()
