from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional, List
from modelsPydantic import modeloUsuario, modeloAuth
from genToken import createToken
from middlewares import BearerJWT
from DB.conexion import Session, engine, Base
from models.modelsDB import User

app= FastAPI(
    title= 'Mi primerAPI 192',
    description= 'Paramétros de API',
    version= '1.0.1'
)

Base.metadata.create_all(bind=engine)


#modelo de validaciopnes


#BD ficticia 
usuarios=[
    {"id": 1,"nombre":"BaruchO","edad":20, "correo":"baruchsaur125@gmail.com"},
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
@app.get('/todosUsuarios/', tags=['Operaciones CRUD'])
def leerUsuarios():
    db = Session()
    try:
        consulta = db.query(User).all()
        return JSONResponse(content=jsonable_encoder(consulta))
    except Exception as e:
        return JSONResponse(status_code=500,
                            content={'message':'Error al consultar',
                                     'error':str(e)})
        
        
#EndPoint buscar por id
@app.get('/buscarUsuario/{id}', tags=['Operaciones CRUD'])
def BuscarUno(id:int):
    db = Session()
    try:
        consultauno = db.query(User).filter(User.id == id).first()
        if not consultauno:
            return JSONResponse(status_code=404,content={'message':'Usuario no encontrado'})
        return JSONResponse(content=jsonable_encoder(consultauno))
    except Exception as e:
        return JSONResponse(status_code=500,
                            content={'message':'Error al consultar',
                                     'error':str(e)})
        
    finally:
        db.close()







#EndPoint Agregar Nuevos
@app.post('/agregarUsuario/', response_model= modeloUsuario ,tags=['Operaciones CRUD'])
def agregarUsuario(usuario:modeloUsuario):
    db = Session()
    try:
        db.add(User(**usuario.model_dump()))
        db.commit()
        return JSONResponse(status_code=201,
                            content={'message':'Usuario guardado',
                                     'usuario':usuario.model_dump()})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,
                            content={'message':'Error al guardar el usuario',
                                     'Excepcioón':str(e)})
    finally:
        db.close()













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