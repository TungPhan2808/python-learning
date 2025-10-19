from fastapi import FastAPI
import logging

logger = logging.getLogger("uvicorn.info")
app = FastAPI(title="To-Do API", docs_url="/docs")

@app.on_event("startup")
async def startup_event():
    # Sử dụng logger của Uvicorn để đảm bảo định dạng nhất quán
    logger.info("Swagger running on http://127.0.0.1:8000/docs (Press CTRL+C to quit)")

from app.routes import auth_routes, todo_routes

app.include_router(auth_routes.router)
app.include_router(todo_routes.router)