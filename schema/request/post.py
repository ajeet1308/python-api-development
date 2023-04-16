from pydantic import BaseModel,Field

class CreatePostRequest(BaseModel):
    title: str = Field(description='title', alias='tl')
    content: str = Field(description='content', alias='ct')
    
    class Config:
        allow_population_by_field_name = True
        underscore_attrs_are_private = True

class UpdatePostRequest(BaseModel):
    title: str = Field(description='title', alias='tl')
    content: str = Field(description='content', alias='ct')
    
    class Config:
        allow_population_by_field_name = True
        underscore_attrs_are_private = True
    