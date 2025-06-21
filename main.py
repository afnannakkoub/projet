from fastapi import FastAPI
from .database import Base, engine
from .routes import user, resource, mood, message
from .routes import user



app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(user.router, prefix="/auth", tags=["Auth"])
app.include_router(resource.router, prefix="/resources", tags=["Resources"])
app.include_router(mood.router, prefix="/moods", tags=["Moods"])
app.include_router(message.router, prefix="/messages", tags=["Messages"])
