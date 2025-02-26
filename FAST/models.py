from pydantic import BaseModel, Field, conint, EmailStr

class modeloUsuario(BaseModel):
    id: int = Field(..., gt=0, description="Id unico y solo numeros positivos")
    nombre: str = Field(..., min_length=3, max_length=50, description="Solo letras: min 3 max 50")
    edad: conint(gt=0, lt=100)
    correo: EmailStr = Field(..., description="Correo electrónico del usuario")