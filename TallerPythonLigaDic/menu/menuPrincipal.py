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
                lb.vw.mostrarResultadosFinales()
            case 4:
                exit()
    except ValueError:
        enter=bool(input('Algo salió mal, presione cualquier tecla para volver a intentar.'))
        menuPrincipal()
            
def registrar():
    print(lb.msg.msgMenuAddEquipo)
    opReg=int(input())
    lb.os.system('cls')
    try:
        match opReg:
            case 1:
                lb.sb.registrarEquipo()
            case 2:
                lb.re.eliminarEquipo()
            case 3:
                lb.vw.verEquipo()
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
    opProg=int(input())
    lb.os.system('cls')
    try:
        match opProg:
            case 1:
                lb.os.system('cls')
                lb.sb.estadisticas()
            case 2:
                lb.os.system('cls')
                lb.sb.programarPartido()
            case 3:
                lb.os.system('cls')
                menuPrincipal()
    except ValueError:
        enter=bool(input(lb.msg.msgError))
        try:
            if enter == True:
                programar()
        except:
            menuPrincipal()