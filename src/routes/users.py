from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder


from src.database import (
    add_user,
    retriev_user,
    retriev_users,
    update_user,
    delete_user
)


from src.models import (
    UserSchema,
    UpdateUserSchema,
    ResponseModel,
    ErrorResponseModel
)


router = APIRouter()


@router.post("/", response_description="Cadastra usuário no banco")
async def add_user_data(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    if new_user:
        return ResponseModel(new_user, "Usuário cadastrado com sucesso.")
    return ErrorResponseModel("Erro:", 404, "Já existe usuario cadastrado com este e-mail")

@router.get("/", response_description="Lista todos os cadastros")
async def get_users():
    users = await retriev_users()
    if users:
        return ResponseModel(users, "Dados de todos os usuários recebidos com sucesso")
    return ResponseModel(users, "Não há usuário cadastrado")


@router.get("/{id}", response_description="Lista usuário especifico conforme id")
async def get_user_data(id):
    user = await retriev_user(id)
    if user:
        return ResponseModel(user, "Dados do usuário recebido com sucesso")
    return ErrorResponseModel("Erro:", 404, "Usuário não encontrado")


@router.put("/{id}", response_description="Atualiza dados dousuário")
async def update_user_data(id: str, req: UpdateUserSchema = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await update_user(id, req)
    if updated_user:
        return ResponseModel(
            "Usuário with ID: {} atualizado com sucesso".format(id),
            "Usuário atualizado com sucesso",
        )
    return ErrorResponseModel(
        "Erro",
        404,
        "Ocorreu erro ao atualizar os dados do usuário",
    )


@router.delete("/{id}", response_description="Deletar usuário")
async def delete_user_data(id: str):
    deleted_user = await delete_user(id)
    if deleted_user:
        return ResponseModel(
            "Usuário com id: {} removido".format(
                id), "Usuário deletado com sucesso"
        )
    return ErrorResponseModel(
        "Erro", 404, "Usuário com id {0} não existe".format(id)
    )
