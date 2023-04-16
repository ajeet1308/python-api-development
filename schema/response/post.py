from pydantic import BaseModel, Field


class Post(BaseModel):
    id: str = Field(description="id ", alias='id')
    title: str = Field(description="title ", alias='tl')
    content: str = Field(description="content ", alias='ct')

    class Config:
        allow_population_by_field_name = True


class GetPostResponse(BaseModel):
    message: str = Field(description="message ", alias='msg')
    data: list[Post] = Field(description="Tat list", alias="dt")

    class Config:
        allow_population_by_field_name = True


class CreatePostResponse(BaseModel):
    message: str = Field(description='message', alias='msg')
    id: str = Field(description='ID', alias='id')

    class Config:
        allow_population_by_field_name = True


class UpdatePostResponse(BaseModel):
    message: str = Field(description='message', alias='msg')
    id: str = Field(description="ID", alias='id')

    class Config:
        allow_population_by_field_name = True

class DeletePostResponse(BaseModel):
    message: str = Field(description="message", alias='msg')
    
    class Config:
        allow_population_by_field_name = True
