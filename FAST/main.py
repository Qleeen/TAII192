from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
    title="Mi primer API 192",
    description="Parámetros de API",
    version="1.0.1"
)

usuarios = [
    {"id": 1, "nombre": "BaruchO", "edad": 20},
    {"id": 2, "nombre": "Fernando", "edad": 22},
    {"id": 3, "nombre": "Max", "edad": 20},
    {"id": 4, "nombre": "Gera", "edad": 25}
]

# Endpoint home
@app.get("/", tags=["Hola Mundo"])
def home():
    return {"hello": "world FastAPI"}

# Endpoint para obtener todos los usuarios
@app.get("/usuarios/", tags=["Operaciones CRUD"])
def leer_usuarios():
    return {"usuarios": usuarios}

# Endpoint para agregar un nuevo usuario
@app.post("/usuarios/", tags=["Operaciones CRUD"])
def agregar_usuario(usuario: dict):
    for usr in usuarios:
        if usr["id"] == usuario.get("id"):
            raise HTTPException(status_code=400, detail="El ID ya existe")
    usuarios.append(usuario)
    return usuario

# Endpoint para modificar un usuario existente
@app.put("/usuarios/{id}", tags=["Operaciones CRUD"])
def modificar_usuario(id: int, usuario_actualizado: dict):
    for usr in usuarios:
        if usr["id"] == id:
            usr["nombre"] = usuario_actualizado.get("nombre", usr["nombre"])
            usr["edad"] = usuario_actualizado.get("edad", usr["edad"])
            return usr
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

# Endpoint para eliminar un usuario
@app.delete("/usuarios/{id}", tags=["Operaciones CRUD"])
def eliminar_usuario(id: int):
    for usr in usuarios:
        if usr["id"] == id:
            usuarios.remove(usr)
            return {"mensaje": "Usuario eliminado"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

# Endpoint para consultar un usuario por ID (parámetro obligatorio)
@app.get("/usuario/{id}", tags=["Parámetro Obligatorio"])
def consulta_usuario(id: int):
    for usu in usuarios:
        if usu["id"] == id:
            return {"mensaje": "Usuario encontrado", "usuario": usu}
    raise HTTPException(status_code=404, detail=f"Usuario no encontrado con ID: {id}")

# Endpoint para consultar un usuario con ID opcional
@app.get("/usuario/", tags=["Parámetro Opcional"])
def consulta_usuario_opcional(id: Optional[int] = None):
    if id is not None:
        for usu in usuarios:
            if usu["id"] == id:
                return {"mensaje": "Usuario encontrado", "usuario": usu}
        return {"mensaje": f"Usuario no encontrado con ID: {id}"}
    return {"mensaje": "No se proporcionó un ID"}

# Endpoint para consultar usuarios con múltiples parámetros opcionales
@app.get("/usuarios/filtrar", tags=["3 parámetros opcionales"])
def consulta_usuarios(
    usuario_id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = [
        usuario for usuario in usuarios
        if (usuario_id is None or usuario["id"] == usuario_id) and
           (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
           (edad is None or usuario["edad"] == edad)
    ]
    
    if resultados:
        return {"usuarios_encontrados": resultados}
    return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}
