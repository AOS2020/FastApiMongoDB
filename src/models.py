from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    nome: str = Field(...)
    password: str = Field(...)
    endereco: str = Field(...)
    bairro: str = Field(...)
    municipio: str = Field(...)
    geolocalizacao: str = Field(...)
    grupo: str = Field(...)
    estabelecimento_comercial: int = Field(...)
    tipo_estabelecimento_comercial: str = Field(...)
    email: EmailStr = Field(...)
    telefone: str = Field(...)
    ativo: int = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "nome": "Senhor das Couves",
                "password": "my_password",
                "endereco": "Rua das batatas",
                "bairro": "Poção",
                "municipio": "Várzea Grande",
                "geolocalizacao": "-15.606223275084467, -56.09443134014695",
                "grupo": "usuário",
                "estabelecimento_comercial": 1,
                "tipo_estabelecimento_comercial": "loja",
                "email": "teste@teste.com",
                "telefone": "6599999999",
                "ativo": 1,
            }
        }


class UpdateUserSchema(BaseModel):
    nome: Optional[str]
    password: Optional[str]
    endereco: Optional[str]
    bairro: Optional[str]
    municipio: Optional[str]
    geolocalizacao: Optional[str]
    grupo: Optional[str]
    estabelecimento_comercial: Optional[int]
    tipo_estabelecimento_comercial: Optional[str]
    email: Optional[EmailStr]
    telefone: Optional[str]
    ativo: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "nome": "Senhor das Couves",
                "password": "my_password",
                "endereco": "Rua das batatas",
                "bairro": "Poção",
                "municipio": "Várzea Grande",
                "geolocalizacao": "-15.606223275084467, -56.09443134014695",
                "grupo": "usuário",
                "estabelecimento_comercial": 1,
                "tipo_estabelecimento_comercial": "loja",
                "email": "teste@teste.com",
                "telefone": "6599999999",
                "ativo": 1,
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
