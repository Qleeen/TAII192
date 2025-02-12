from fastapi import FastAPI, HTTPException
from typing import Optional

app= FastAPI(
    title= 'Mi primerAPI 192',
    description= 'Paramétros de API',
    version= '1.0.1'
)

usuarios=[
    {"id": 1,"nombre":"BaruchO","edad":20},
    {"id": 2,"nombre":"Fernando","edad":22},
    {"id": 3,"nombre":"Max","edad":20},
    {"id": 4,"nombre":"Gera","edad":25}
]

#Endpoint home

@app.get('/', tags=['Hola Mundo'])
def home():
    return {'hello':'world FastAPI'}

#EndPoint COnsulta Usuarios
@app.get('/todosUsuarios/', tags=['Operaciones CRUD'])
def leerUsuarios():
    return {"Los usuarios registrados son":usuarios}

#EndPoint Agregar Nuevos
@app.post('/agregarUsuario/', tags=['Operaciones CRUD'])
def agregarUsuario(usuario:dict):
    for usr in usuarios:
        if usr["id"] == usuario.get("id"):
            raise HTTPException(status_code=400, detail="El ID ya existe")
    usuarios.append(usuario)
    return usuario

#EndPoint Modificar Usuario
@app.put('/modificarUsuario/{id}', tags=['Operaciones CRUD'])
def modificarUsuario(id:int, usuario:dict):
    for usr in usuarios:
        if usr["id"] == usuario.get("id"):
            usr["nombre"] = usuario.get("nombre")
            usr["edad"] = usuario.get("edad")
            return usuario
    raise HTTPException(status_code=400, detail="Usuario no coincide con el ID")







# #Endpoint promedio
# @app.get('/promedio', tags=['Mi calificacion TAI'])
# def promedio():
#     return 10


# #Endpoint parametros Obligatorios
# @app.get('/usuario/{id}', tags=['Parámetro Obligatorio'])
# def consultaUsuario(id:int):
#     #Conectamos a la BD
#     #Consultamos
#     return {'Se encontró el usuario':id}

# #Endpoint parametros Opcionales
# @app.get('/usuario/', tags=['Parámetro Opcional'])
# def consultaUsuario2(id:Optional[int]= None):
#     if id is not None:
#         for usu in usuarios:
#             if usu["id"] == id:
#                 return {"mensaje": "Usuario encontrado", "usuario": usu}
#         return {"mensaje":f"Usuario no encontrado con el id : {id}"}
#     else:
#         return {"mensaje":"No se proporciono un ID"}
    
    
# #endpoint con varios parametro opcionales
# @app.get("/usuarios/", tags=["3 parámetros opcionales"])
# async def consulta_usuarios(
#     usuario_id: Optional[int] = None,
#     nombre: Optional[str] = None,
#     edad: Optional[int] = None
# ):
#     resultados = []

#     for usuario in usuarios:
#         if (
#             (usuario_id is None or usuario["id"] == usuario_id) and
#             (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
#             (edad is None or usuario["edad"] == edad)
#         ):
#             resultados.append(usuario)

#     if resultados:
#         return {"usuarios_encontrados": resultados}
#     else:
#         return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}