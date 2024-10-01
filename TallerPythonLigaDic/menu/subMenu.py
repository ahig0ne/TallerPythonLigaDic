import ligabet as lb
def registrarEquipo():
    print(lb.msg.msgMenuEquipo)
    opRegEquipo=int(input())
    lb.os.system('cls')
    try:
        match opRegEquipo:
            case 1:
                lb.os.system('cls')
                lb.re.registroNuevoEquipo()
            case 2:
                lb.os.system('cls')
                lb.eq.agregarJugadores()
            case 3:
                lb.os.system('cls')
                lb.eq.agregarCuerpoTecnico()
            case 4:
                lb.os.system('cls')
                lb.eq.agregarCuerpoMedico()
            case 5:
                lb.os.system('cls')
                lb.main.registrar()
    except ValueError:
        enter=bool(input(lb.msg.msgError))
        try:
            if enter == True:
                lb.os.system('cls')
                registrarEquipo()
        except ValueError:
            registrarEquipo()

def estadisticas():
    print(lb.msg.msgMenuEstadisticas)
    opStat=int(input())
    try:
        match opStat:
            case 1:
                lb.os.system('cls')
                lb.st.menuEstadisticas()
            case 2:
                lb.os.system('cls')
                lb.sb.menuJugadores()
            case 3:
                lb.os.system('cls')
                lb.main.programar()
    except ValueError:
        enter=bool(input(lb.msg.msgError))
        try:
            if enter == True:
                lb.os.system('cls')
                lb.main.programar()
        except:
            lb.os.system('cls')
            lb.main.menuPrincipal()

def programarPartido():
    lb.rep.resultadoPartido()

def menuJugadores():
    lb.os.system('cls')
    print(lb.msg.msgJugadorEst)
    opMenJug=int(input())
    try:
        match opMenJug:
            case 1:
                lb.os.system('cls')
                lb.rep.menuReportarTarjetas()
                
            case 2:
                lb.os.system('cls')
                lb.st.menuEstadisticas()
            case 3:
                lb.os.system('cls')
                lb.main.programar()
    except ValueError:
        enter=bool(input(lb.msg.msgError))
        try:
            if enter == True:
                lb.os.system('cls')
                lb.main.programar()
        except:
            lb.os.system('cls')
            lb.main.menuPrincipal()