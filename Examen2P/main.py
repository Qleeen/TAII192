from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from typing import Optional, List
from pydantic import BaseModel, Field


app= FastAPI(
    title= 'Mi primerAPI 192',
    description= 'Paramétros de API',
    version= '1.0.1'
)


@app.get('/', tags=['Hola Mundo'])
def home():
    return {'hello':'world FastAPI'}


#Api registro de conductores Nombre, tipo licencia, no.licencia
conductores = [
    {"nombre": "Baruch", "tipo_licencia": "A", "licencia": "12345678912a"},
    {"nombre": "Fernando", "tipo_licencia": "D", "licencia": "182473829123"},
    {"nombre": "Isay", "tipo_licencia": "B", "licencia": "172839123123"},
    {"nombre": "Max", "tipo_licencia": "C", "licencia": "938475392817"},
    {"nombre": "Yahir", "tipo_licencia": "A", "licencia": "193745920182"},
]

class modeloConductor(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=50, description="Solo letras: min 3 max 50")
    tipo_licencia: str = Field(..., max_length=1, description="Ingresa el tipo de licencia, A, B, C, D")
    licencia: str = Field(..., min_length=12, max_length=12, description="Ingresa el numero de licencia")
    
    
    
#Endpoint para registrar conductores
@app.post('/RegistrarConductor', response_model= modeloConductor ,tags=['RegistrarConductor'])
def agregarConductor(conductor:modeloConductor):
    for c in conductores:
        if c['licencia'] == conductor.licencia:
            raise HTTPException(status_code=400, detail="Conductor ya registrado")
    conductores.append(conductor)
    return conductor

#Endpoint para consultar conductor 
@app.get('/LeerConductor/{licencia}',tags=['ObtenerConductor'])
def leerConductor(licencia: str):
    for conductor in conductores:
        if conductor['licencia'] == licencia:
            return conductor
    raise HTTPException(status_code=404, detail="Conductor no encontrado")

#Endpoint para eliminar conductor
@app.delete('/EliminarConductor/{licencia}', tags=['EliminarConductores'])
def eliminarConductor(licencia: str):
    for conductor in conductores:
        if conductor['licencia'] == licencia:
            conductores.remove(conductor)
            return {"mensaje": "Conductor eliminado"}
    raise HTTPException(status_code=404, detail="Conductor no encontrado")

