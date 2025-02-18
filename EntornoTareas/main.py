from fastapi import FastAPI, HTTPException
from datetime import date

app = FastAPI(
    title='Api EntornoTareas',
    description='Primer Repaso',
    version='1.0.1'
)

tareas = [
    {"id": 1, "titulo": "Tarea 1", "descripcion": "Descripción de la tarea 1", "fecha_vencimiento": date(2023, 12, 31), "completada": False},
    {"id": 2, "titulo": "Tarea 2", "descripcion": "Descripción de la tarea 2", "fecha_vencimiento": date(2023, 11, 30), "completada": True},
    {"id": 3, "titulo": "Tarea 3", "descripcion": "Descripción de la tarea 3", "fecha_vencimiento": date(2023, 10, 31), "completada": False},
    {"id": 4, "titulo": "Tarea 4", "descripcion": "Descripción de la tarea 4", "fecha_vencimiento": date(2023, 9, 30), "completada": True}
]

# Endpoint home
@app.get('/', tags=['Hola Mundo'])
def home():
    return {'hello': 'world FastAPI'}

# EndPoint Obtener todas las tareas.
@app.get("/tareas", tags=['Listado de todas las tareas'])
def obtenerTareas():
    return tareas

# Enpoint Obtener una tarea específica por su ID.
@app.get("/tareasID/{tarea_id}", tags=['Obtener una tarea por ID'])
def tareasID(tarea_id: int):
    for tarea in tareas:
        if tarea["id"] == tarea_id:
            return tarea
    raise HTTPException(status_code=400, detail="Tarea no encontrada")

# Enpoint Crear una nueva tarea.
@app.post("/tareasCrear", tags=['Crear nueva tarea'])
def tareasCrear(tarea: dict):
    for t in tareas:
        if t["id"] == tarea["id"]:
            raise HTTPException(status_code=400, detail="El ID ya existe")
    tareas.append(tarea)
    return tarea

# Enpoint Actualizar una tarea existente.
@app.put("/tareasActualizar/{tarea_id}", tags=['Actualizar tareas'])
def tareasActualizar(tarea_id: int, tarea_actualizada: dict):
    for index, tarea in enumerate(tareas):
        if tarea["id"] == tarea_id:
            tareas[index] = tarea_actualizada
            return tarea_actualizada
    raise HTTPException(status_code=400, detail="Tarea no encontrada")

# Enpoint Eliminar una tarea existente.
@app.delete("/tareasEliminar/{tarea_id}", tags=['Eliminar Tareas'])
def tareasEliminar(tarea_id: int):
    for index, tarea in enumerate(tareas):
        if tarea["id"] == tarea_id:
            tarea_eliminada = tareas.pop(index)
            return tarea_eliminada 
    raise HTTPException(status_code=400, detail="Tarea no encontrada")
