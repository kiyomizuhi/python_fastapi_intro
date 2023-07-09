from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers import task, done

app = FastAPI()
app.include_route(task.router)
app.include_route(done.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



