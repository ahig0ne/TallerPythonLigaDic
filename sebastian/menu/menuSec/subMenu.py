import ligabet as lb
def registrarEquipo():
    print(lb.msg.msgAddEquipo)
    opRegEquipo=int(input())
    try:
        match opRegEquipo:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                lb.main.menuPrincipal()
    except ValueError:
        enter=bool(input(lb.msg.msgError))
        try:
            if enter == True:
                registrarEquipo()
        except ValueError:
            lb.main.menuPrincipal()