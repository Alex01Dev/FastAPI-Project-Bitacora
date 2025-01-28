'''
Inicializar el proyecto en FastAPI
'''
from fastapi import FastAPI, HTTPException
from typing import List
from uuid import UUID, uuid4
from models import Usuario, Gender, Role, UpdateUser

app = FastAPI()
db : List[Usuario] = [
     Usuario(
        id= uuid4(),
        name= "Alex Amauri",
        last_name= "Marquez Canales",
        gender= Gender.Male,
        roles= [Role.admin],

    ),
    Usuario(
        id= uuid4(),
        name= "Carlos Jesus",
        last_name= "Carballo Horseman",
        gender= Gender.Other,
        roles= [Role.user],
         
    ),
    Usuario(
        id= uuid4(),
        name= "Alina",
        last_name= "Bonilla Paredes",
        gender= Gender.Female,
        roles= [Role.user],
         
    )
]

@app.get("/")
async def roo():
    '''Funcion de bienvenida'''
    return "Welcome: Hello friends"

# @app.get("/calculation")
# async def calculation_age(year_date: int, year_actually: int):
#     '''Funcion para calcular la edad'''
#     age: int = year_actually - year_date
#     return age

# print("You age is: ",calculation_age(2004,2025))

@app.get("/api/getUsers")
async def get_users():
    return db

@app.post("/api/insertUser")
async def send_users(usuario: Usuario):
    db.append(usuario)
    return {id: usuario.id}

@app.delete("/api/deleteUser/{id}")
async def delete_user(id: UUID):
    for usuario in db:
        if usuario.id == id:
            db.remove(usuario)
            return
    raise HTTPException(status_code=404, detail=f"Error deleting id: {id} fail")

@app.put("/api/updateUser/{id}")
async def update_user(user_update: UpdateUser, id: UUID):
    for usuario in db:
        if usuario.id == id:
            if user_update.name is not None:
                usuario.name = user_update.name
            if user_update.last_name is not None:
                usuario.last_name = user_update.last_name
            if user_update.gender is not None:
                usuario.gender = user_update.gender
            if user_update.roles is not None:
                usuario.roles = user_update.roles
            return {"message": f"User with id {id} updated successfully", "user": usuario}
    raise HTTPException(status_code=404, detail=f"User with id {id} not found")
