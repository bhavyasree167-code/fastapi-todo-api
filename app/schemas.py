from pydantic import BaseModel, Field

class TodoCreate(BaseModel):

   title: str = Field(
    ...,
    min_length=3,
    max_length=200
)

class TodoResponse(BaseModel):

    id: int
    title: str
    completed: bool

    class Config:
        from_attributes = True