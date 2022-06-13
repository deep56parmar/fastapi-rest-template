from fastapi import FastAPI
from routers import user
from config.db import connectDB
from dotenv import load_dotenv


load_dotenv()
connectDB()
app = FastAPI()
app.include_router(user.router)
