from pydantic import BaseModel, EmailStr, Field

class CustomerResponse(BaseModel):
    id: str
    object: str = Field(pattern="^customer$")
    email: EmailStr
    name: str