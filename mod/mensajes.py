import index as ix

menuPrincipal ="""
    ___________________________________________
   /                                          /
  / ---         LIGA BETPLAY 2024         ---/
 /__________________________________________/

    -1. Registrar equipo

    -2. Programar partido

    -3. Resultados

    -4. Salir
"""

#ingresar el menu secundario de registrar un equipo.
menuRegEquipo = """
    
           | MENU EQUIPO |

    -1. Agregar Equipo

    -2. Volver a menu principal

"""

menuAddJugadores = """

            | REGISTRAR EQUIPO |

    -1. Registrar equipo

    -2. Ver equipos

    -3. Volver a menu anterior

"""
menuAddEquipo = """
            | REGISTRAR EQUIPO |

    -Por favor ingrese nombre del equipo: 

"""
menuDelEquipo = f"""
            | AGREGAR JUGADORES |

    -Escriba cantidad de jugadores en el equipo: 

"""

menuAddJugador = """

Jugador con camisa: 

"""

menuPosicionJugador = """

1. Portero
2. Defensa
3. Lateral
4. Medio Campo
5. Delantero

Posicion del jugador:

"""

menuTercero = """

        | Estadisticas y Programacion de Partidos |

    -1. Ver estadisticas de los equipos

    -2. Programar partido

    -3. Regresar al menu anterior

"""

menuProgPartido = """
INGRESE MES
"""

menuProgPartido2 = """
AGREGAR FECHA DE PARTIDO
INGRESE DIA

"""

menuFechaPartido=f"""
la fecha del partido es {ix.dia}/{ix.mes}/2024
"""

despedida="""


Muchas gracias por utilizar este programa para crear Liga BetPlay.


Hasta pronto!



"""

error = """
Algo salió mal, pulsa la tecla enter para volver a escribir, cualquier palabra para volver al menu anterior.
"""

