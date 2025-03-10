from pydantic import BaseModel, Field, EmailStr

class modeloUsuario(BaseModel):
    id: int = Field(..., gt=0, description="Id unico y solo numeros positivos")
    nombre: str = Field(..., min_length=3, max_length=50, description="Solo letras: min 3 max 50")
    edad: int = Field(..., ge=1, le=121, description="Ingrese su edad")
    correo: EmailStr = Field(..., description="Correo electrónico del usuario")

class modeloAuth(BaseModel):
    correo: EmailStr = Field(..., description="Correo electrónico del usuario", example="baruchsaur125@gmail.com")
    passw: str= Field(..., min_lenght=8,strip_whitespace=True, example="Contraseña minimo 8 caracteres")
    