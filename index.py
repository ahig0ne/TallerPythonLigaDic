import os
import mod.mensajes as msg
import mod.funciones as funct
import mod.equipos as eq
import mod.reportes as rp

player = []
ligaBetPlay = []
goles = 0
partidos = 0
dia = 0
mes = 0
###[equipoNombre,0,0,0,0,0,0,0]
#PJ = 2     PG = 3      PP = 4      PE = 5
#GF = 6     GC = 7      TP = 8
os.system('cls')

if (__name__ == "__main__"):
    os.system('cls')
    valorMenu = False
    funct.menuPrincipal()