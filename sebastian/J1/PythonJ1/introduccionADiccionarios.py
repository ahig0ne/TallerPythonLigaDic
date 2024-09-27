alumnos = {}
alumno = {

    'nombre':'Jose',
    'notas':{
        'parciales':{
        'p1': 0.0,
        'p2': 0.0,
        'p3': 0.0,
    },
    'quices':[1],
    'trabajos':[]
    }
}
alumnos.update ({str(1).zfill(4):alumno})
alumno = {

    'nombre':'Miguel',
    'notas':{
        'parciales':{
        'p1': 0.0,
        'p2': 0.0,
        'p3': 0.0,
    },
    'quices':[2],
    'trabajos':[]
    }
}
alumnos.update ({str(2).zfill(4):alumno})
print(alumnos[str(2).zfill(4)])

for key in alumnos:
    print(alumnos.get(key,'error').get('notas','-1').get('quices')[0])

palabra = input('Ingrese codigo a buscar').zfill(4)
miAlumno = alumnos.get(palabra-1)
if (type(miAlumno) == int):
    print('bueno')
elif (type(miAlumno) == dict):
    print(miAlumno.get('nombre'))

try:
    print(miAlumno.get('nombre'))
except:
    print('No existe el dato')