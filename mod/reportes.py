import index as ix

def resultadoPartido():
    ix.os.system('cls')
    equipoLocal = input("Ingresa el nombre del Local: ")
    equipoVisit = input("Ingresa el nombre del visitante: ")
    golesEquipoLocal = int(input(f"Ingrese los goles de {equipoLocal}: "))
    golesEquipoVisit = int(input(f"Ingrese los goles de {equipoVisit}: "))

    equipoLocalEncontrado = None
    equipoVisitEncontrado = None

    for ix.player in ix.ligaBetPlay:
        if ix.player[0] == equipoLocal:
            equipoLocalEncontrado = ix.player
        elif ix.player[0] == equipoVisit:
            equipoVisitEncontrado = ix.player

    # Verificar que ambos equipos existen
    if equipoLocalEncontrado is None:
        print(f'Equipo {equipoLocal} no existe en la liga.')
        resultadoPartido()
    if equipoVisitEncontrado is None:
        print(f'Equipo {equipoVisit} no existe en la liga.')
        resultadoPartido()

    equipoLocalEncontrado[2] += 1  # Partidos jugados
    equipoLocalEncontrado[6] += golesEquipoLocal  # Goles a favor
    equipoLocalEncontrado[7] += golesEquipoVisit  # Goles en contra

    if golesEquipoLocal > golesEquipoVisit:
        equipoLocalEncontrado[3] += 1
        equipoLocalEncontrado[8] += 3
        ix.funct.menuPrincipal()
    elif golesEquipoLocal == golesEquipoVisit:
        equipoLocalEncontrado[5] += 1
        equipoLocalEncontrado[8] += 1
        ix.funct.menuPrincipal()
    else:
        equipoLocalEncontrado[4] += 1
        ix.funct.menuPrincipal()

    equipoVisitEncontrado[2] += 1
    equipoVisitEncontrado[6] += golesEquipoVisit
    equipoVisitEncontrado[7] += golesEquipoLocal

    if golesEquipoVisit > golesEquipoLocal:
        equipoVisitEncontrado[3] += 1 
        equipoVisitEncontrado[8] += 3
        ix.funct.menuPrincipal()
    elif golesEquipoVisit == golesEquipoLocal:
        equipoVisitEncontrado[5] += 1 
        equipoVisitEncontrado[8] += 1
        ix.funct.menuPrincipal()
    else:
        equipoVisitEncontrado[4] += 1
        ix.funct.menuPrincipal()

def imprimirEquipoConMasPuntos():
    puntosMaximos = -1
    for equipo in ix.ligaBetPlay:
        if equipo[8] > puntosMaximos:
            puntosMaximos = equipo[8]
            equipoGanador = equipo[0]
    print(f"El equipo con más puntos es: {equipoGanador} con {puntosMaximos} puntos.")