import ligabet as lb
def menuPrincipal():
    print(lb.msg.msgMenuPrincipal)
    opMain=int(input())
    try:
        match opMain:
            case 1:
                registrar()
            case 2:
                programar()
            case 3:
                resultados()
            case 4:
                exit
    except ValueError:
        enter=bool(input('Algo salió mal, presione cualquier tecla para volver a intentar.'))
        menuPrincipal()
            
def registrar():
    print(lb.msg.msgMenuAddEquipo)
    opReg=int(input())
    try:
        match opReg:
            case 1:
                lb.equipo['nombre'] = input(lb.msg.msgAddEquipo)
                numeroEquipo = str(len(lb.equipo)+1).zfill(2)
                lb.equipo.update({numeroEquipo:lb.equipo})
                registrar()
            case 2:
                lb.sb.borrarEquipo()
            case 3:
                lb.eq.verEquipo()
                pass
            case 4:
                menuPrincipal()
    except ValueError:
        enter=bool(input(lb.msg.msgError))
        try:
            if enter == True:
                menuPrincipal()
        except ValueError:
            registrar()

def programar():
    print(lb.msg.msgMenuEstProg)
    opProg=int(input)
    try:
        match opProg:
            case 1:
                lb.sb.estadisticas()
            case 2:
                lb.sb.programarPartido()
            case 3:
                menuPrincipal()
    except ValueError:
        enter=bool(input(lb.msg.msgError))
        try:
            if enter == True:
                programar()
        except:
            menuPrincipal()

def resultados():
    pass