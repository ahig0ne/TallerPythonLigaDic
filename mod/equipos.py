import index as ix
def crearEquipo():
    equipoNombre = str(input(ix.msg.menuAddEquipo))
    ix.os.system('cls')
    print(ix.msg.menuDelEquipo
    jugadores=int(input())
    for i in range(0, jugadores):
        i+=1
        ix.os.system('cls')
        jugador=str(input(f'Ingrese nombre del jugador con el dorsal {i}: '))
        print(ix.msg.menuPosicionJugador)
        posicion = input()
        match posicion:
            case '1':
                posicionJugador = 'Portero'
            case '2':
                posicionJugador = 'Defensa'
            case '3':
                posicionJugador = 'Lateral'
            case '4':
                posicionJugador = 'Medio Campo'
            case '5':
                posicionJugador = 'Delantero'
            case _:
                print ('Seleccione numero correctamente: ')
        ix.player.append([jugador, i, posicionJugador])
    ix.ligaBetPlay.append([equipoNombre, ix.player, 0 , 0 , 0 , 0 , 0, 0 , 0])
    ix.funct.menuAgregarEquipo()
def equiposCuentas():
    for equipo in ix.ligaBetPlay:
        print(equipo)
    ix.funct.menuAgregarEquipo()

