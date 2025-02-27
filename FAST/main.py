from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from typing import Optional, List
from modelsPydantic import modeloUsuario, modeloAuth
from genToken import createToken



app= FastAPI(
    title= 'Mi primerAPI 192',
    description= 'Paramétros de API',
    version= '1.0.1'
)




#modelo de validaciopnes


#BD ficticia 
usuarios=[
    {"id": 1,"nombre":"BaruchO","edad":20, "correo":"example1@example.com"},
    {"id": 2,"nombre":"Fernando","edad":22, "correo":"example2@example.com"},
    {"id": 3,"nombre":"Max","edad":20, "correo":"example3@example.com"},
    {"id": 4,"nombre":"Gera","edad":25, "correo":"example4@example.com"},
]
     
    
    
    
    
    


#Endpoint home
@app.get('/', tags=['Hola Mundo'])
def home():
    return {'hello':'world FastAPI'}

#EndPoint Autenticación
@app.post('/auth', tags=['Autentificacion'])
def login(autorizacion:modeloAuth):
    if autorizacion.correo == 'baruchsaur125@gmail.com' and autorizacion.passw == '12345678':
        token:str = createToken(autorizacion.model_dump())
        print(token)
        return JSONResponse(token)
    else:
        return "Aviso: COntraseña incorrecta"




#EndPoint COnsulta Usuarios
@app.get('/todosUsuarios/', response_model= List[modeloUsuario] ,tags=['Operaciones CRUD'])
def leerUsuarios():
    return usuarios

#EndPoint Agregar Nuevos
@app.post('/agregarUsuario/', response_model= modeloUsuario ,tags=['Operaciones CRUD'])
def agregarUsuario(usuario:modeloUsuario):
    for usr in usuarios:
        if usr["id"] == usuario.id:
            raise HTTPException(status_code=400, detail="El ID ya existe")
    usuarios.append(usuario)
    return usuario

#EndPoint Modificar Usuario
@app.put('/modificarUsuario/{id}', response_model= modeloUsuario, tags=['Operaciones CRUD'])
def modificarUsuario(id:int, usuarioAcrtualizado:modeloUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index] = usuarioAcrtualizado.model_dump()
            return usuarios[index]
    raise HTTPException(status_code=400, detail="Usuario no encontrado")

#EndPoint Eliminar Usuario
@app.delete('/eliminarUsuario/{id}', tags=['Operaciones CRUD'])
def eliminarUsuario(id:int):
    for usr in usuarios:
        if usr["id"] == id:
            usuarios.remove(usr)
            return {"mensaje":"Usuario eliminado"}
    raise HTTPException(status_code=400, detail="Ya se elimino el usuario")






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