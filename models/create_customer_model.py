from pydantic import BaseModel

class CustomerResponse(BaseModel):
    id: str
    email: str
    name: str
    object: str