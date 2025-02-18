from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date

app = FastAPI(
    title='Api EntornoTareas',
    description='Primer Repaso',
    version='1.0.1'
)

class Tarea(BaseModel):
    id: int
    titulo: str
    descripcion: str
    fecha_vencimiento: date
    completada: bool

tareas = []

# Endpoint home
@app.get('/', tags=['Hola Mundo'])
def home():
    return {'hello': 'world FastAPI'}

# EndPoint Obtener todas las tareas.
@app.get("/tareas", response_model=list[Tarea], tags=['Listado de todas las tareas'])
def obtenerTareas():
    return tareas

# Enpoint Obtener una tarea específica por su ID.
@app.get("/tareasID/{tarea_id}", response_model=Tarea, tags=['Obtener una tarea por ID'])
def tareasID(tarea_id: int):
    for tarea in tareas:
        if tarea.id == tarea_id:
            return tarea
    raise HTTPException(status_code=400, detail="Tarea no encontrada")

# Enpoint Crear una nueva tarea.
@app.post("/tareasCrear", response_model=Tarea, tags=['Crear nueva tarea'])
def tareasCrear(tarea: Tarea):
    for t in tareas:
        if t.id == tarea.id:
            raise HTTPException(status_code=400, detail="El ID ya existe")
    tareas.append(tarea)
    return tarea

# Enpoint Actualizar una tarea existente.
@app.put("/tareasActualizar/{tarea_id}", response_model=Tarea, tags=['Actualizar tareas'])
def tareasActualizar(tarea_id: int, tarea_actualizada: Tarea):
    for index, tarea in enumerate(tareas):
        if tarea.id == tarea_id:
            tareas[index] = tarea_actualizada
            return tarea_actualizada
    raise HTTPException(status_code=400, detail="Tarea no encontrada")

# Enpoint Eliminar una tarea existente.
@app.delete("/tareasEliminar/{tarea_id}", response_model=Tarea, tags=['Eliminar Tareas'])
def tareasEliminar(tarea_id: int):
    for index, tarea in enumerate(tareas):
        if tarea.id == tarea_id:
            tarea_eliminada = tareas.pop(index)
            return tarea_eliminada 
    raise HTTPException(status_code=400, detail="Tarea no encontrada")