import ligabet as lb

def registroNuevoEquipo():
    equipo={
        'nombre':'',
        'estadisticas':{
            'PJ':0,
            'PG':0,
            'PP':0,
            'PE':0,
            'GF':0,
            'GC':0,
            'TP':0,
            'TA':0,
            'TR':0,
            'TT':0
        },
        'jugadores':{}
        
        }
    equipo['nombre'] = input(lb.msg.msgAddEquipo)
    numeroEquipo = str(len(lb.ligaBetPlay) +1 ).zfill(2)
    lb.ligaBetPlay[numeroEquipo] = equipo
    lb.equipos+=1                
    print(f'El equipo {equipo}, se ha creado')
    lb.sb.registrarEquipo()

def eliminarEquipo():
    try:
        if not lb.ligaBetPlay:
            print('No hay equipos disponibles para eliminar.')
            lb.sb.registrarEquipo()

        print('\nEquipos disponibles:')
        for numero, equipo in lb.ligaBetPlay.items():
            print(f'{numero}: {equipo['nombre']}')

        numeroEquipo = input('Ingrese el número del equipo que desea eliminar: ')
        if numeroEquipo not in lb.ligaBetPlay:
            print('Equipo no encontrado.')
            lb.main.registrar()

        equipoEliminado = lb.ligaBetPlay.pop(numeroEquipo)
        lb.equipos -= 1
        print(f'El equipo {equipoEliminado['nombre']} ha sido eliminado correctamente.')
        lb.sb.registrarEquipo()

    except ValueError as e:
        print(e)
    except Exception as e:
        print(f'Ocurrió un error inesperado: {e}')