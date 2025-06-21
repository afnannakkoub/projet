from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str

    class Config:
        orm_mode = True

# Resource
class ResourceBase(BaseModel):
    title: str
    content: str
    type: str

class ResourceCreate(ResourceBase): pass
class ResourceOut(ResourceBase):
    id: int
    class Config: orm_mode = True

# Mood
class MoodCreate(BaseModel):
    mood: str
    note: Optional[str] = None

class MoodOut(MoodCreate):
    id: int
    date: datetime
    class Config: orm_mode = True

# Message
class MessageCreate(BaseModel):
    content: str

class MessageOut(MessageCreate):
    id: int
    timestamp: datetime
    class Config: orm_mode = True
