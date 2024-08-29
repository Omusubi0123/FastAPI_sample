from fastapi import FastAPI
from app.routes import item_routes, user_routes

app = FastAPI()

app.include_router(item_routes.router, prefix="/items")
app.include_router(user_routes.router, prefix="/users")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}
