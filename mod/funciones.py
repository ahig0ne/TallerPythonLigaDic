import index as ix

def menuPrincipal():
    ix.os.system('cls')
    valorMenu=True
    while valorMenu!=False:
        print(ix.msg.menuPrincipal)
        opPrincipal = input()
        match opPrincipal:
            case '1':
                ix.os.system('cls')
                opPrincipal = 0
                valorMenu= False
                menuSecundarioUno()
            case '2':
                ix.os.system('cls')
                openPrincipal = 0
                valorMenu = False
                menuSecundarioDos()
            case '3':
                ix.rp.imprimirEquipoConMasPuntos()
                exit
            case '4':
                ix.os.system('cls')
                print(ix.msg.despedida)
                break
            case _:
                ix.os.system('cls')
                print('Escriba opcion valida: ')
#crear equipo
def menuSecundarioUno():
    ix.os.system('cls')
    valorMenuSec=True
    while valorMenuSec!= False:
        print(ix.msg.menuRegEquipo)
        opRegEquipo = input()
        match opRegEquipo:
            case '1':
                ix.os.system('cls')
                opRegEquipo = 0
                valorMenuSec = False
                menuAgregarEquipo()
            case '2':
                ix.os.system('cls')
                opRegEquipo = 0
                valorMenuSec = False
                menuPrincipal()
            case _:
                ix.os.system('cls')
                print('Escriba opcion valida: ')

def menuAgregarEquipo():
    valueAgregarEquipo=True
    while valueAgregarEquipo!=False:
        print(ix.msg.menuAddJugadores)
        opAddJug= input()
        match opAddJug:
            case '1':
                valueAgregarEquipo = False
                ix.eq.crearEquipo()
            case '2':
                valueAgregarEquipo = False
                ix.os.system('cls')
                ix.eq.equiposCuentas()
            case '3':
                menuSecundarioUno()
            case _:
                print('Escriba opcion valida: ')
                menuAgregarEquipo()

def menuSecundarioDos():
    valorMenuSec= True
    while valorMenuSec != False:
        print(ix.msg.menuTercero)
        opMenuTres = input()
        match opMenuTres:
            case '1':
                valorMenuSec=False
                for i in ix.ligaBetPlay:
                    print(i)
                menuSecundarioDos()
            case '2':
                valorMenuSec=False
                ix.rp.resultadoPartido()
            case '3':
                valorMenuSec=False               
                menuPrincipal()
            case _:
                ix.os.system('cls')
                print('Escriba opcion valida: ')

                    