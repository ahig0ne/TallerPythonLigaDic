import os
import utils.mensajes as msg
import menu.menuPrincipal as main
import menu.subMenu as sb
import modulosCreacion.registroEquipoInfo as eq
import modulosCreacion.registroEquipo as re
import view.ver as vw
import utils.reportes as rep
import utils.estadisticas as st

ligaBetPlay={}
cuerpoMedico={
    'medico':''
}
equipos=0
###[equipoNombre,0,0,0,0,0,0,0]
#PJ = 2     PG = 3      PP = 4      PE = 5
#GF = 6     GC = 7      TP = 8
os.system('cls')

if (__name__ == "__main__"):
    os.system('cls')
    valorMenu = False
    main.menuPrincipal()