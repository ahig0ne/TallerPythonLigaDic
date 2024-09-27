import os
import menu.mensajes as msg
import menu.menuPrincipal as main
import menu.menuSec.subMenu as sb
import menu.menuSec.menuTer.equipo as eq

ligaBetPlay={}
equipo={
        'nombre':'',
        'estadisticas':{
            'PJ':0,
            'PG':0,
            'PP':0,
            'PE':0,
            'GF':0,
            'GC':0,
            'TP':0
        }
}
jugadores={
    'nombre':'',
    'numero':0,
    'posición':'',
    'goles':0,
    'TR':0,
    'TA':0,
    'Faltas':0
}
cuerpoTecnico={
    'tecnico':'',
    'asistente':'',
    'prepFisico':''
}
cuerpoMedico={
    'medico':''
}
numEq=0
###[equipoNombre,0,0,0,0,0,0,0]
#PJ = 2     PG = 3      PP = 4      PE = 5
#GF = 6     GC = 7      TP = 8
os.system('cls')

if (__name__ == "__main__"):
    os.system('cls')
    valorMenu = False
    main.menuPrincipal()