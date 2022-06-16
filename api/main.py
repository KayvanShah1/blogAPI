from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from api.routes import templates
from api.routes import users

app = FastAPI()

# Handle CORS protection
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# register all the APIRouter Endpoints
app.include_router(templates.router)
app.include_router(users.router)

# Static Files and Templates
app.mount("/static", StaticFiles(directory="./static"), name="static")
