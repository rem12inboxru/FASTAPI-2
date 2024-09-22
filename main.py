from fastapi import FastAPI, Path
import uvicorn
from typing import Annotated

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": f"Главная страница"}


@app.get("/user/admin")
async def admin() -> dict:
    return {"message": f"Вы вошли как администратор"}

@app.get("/user/{name}/{age}")
async def name_age(name: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
                   age: int = Path(ge=18, le=120, description="Enter age", example=119)) -> dict:
    return {"message": f"Информация о пользователе. Имя {name}. Возраст {age}"}


@app.get("/user/{user_id}")
async def user_id_in(user_id: int = Path(ge=1, le=100, description="Enter User ID", example=99)) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}




if __name__ == '__main__':
    uvicorn.run(app="main:app", reload=True)
