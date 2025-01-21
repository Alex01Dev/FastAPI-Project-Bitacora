'''
Inicializar el proyecto en FastAPI
'''
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def roo():
    '''Funcion de bienvenida'''
    return "Welcome: Hello friends"

@app.get("/calculation")
async def calculation_age(year_date: int, year_actually: int):
    '''Funcion para calcular la edad'''
    age: int = year_actually - year_date
    return age

print("You age is: ",calculation_age(2004,2025))
