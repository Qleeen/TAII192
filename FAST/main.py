from fastapi import FastAPI

app= FastAPI(
    title= 'Mi primerAPI 192',
    description= 'Paramétros de API',
    version= '1.0.1'
)

#Endpoint home

@app.get('/', tags=['Hola Mundo'])
def home():
    return {'hello':'world FastAPI'}

#Endpoint promedio
@app.get('/promedio', tags=['Mi calificacion TAI'])
def promedio():
    return 10


#Endpoint parametros Obligatorios
@app.get('/usuario/{id}', tags=['parámetro Obligatorio'])
def consultaUsuario(id:int):
    #Conectamos a la BD
    #Consultamos
    return {'Se encontró el usuario':id}