from fastapi import APIRouter, Request

from service import post_service

from schema.response import GetPostResponse, UpdatePostResponse, CreatePostResponse, DeletePostResponse
from schema.request import CreatePostRequest, UpdatePostRequest

post_router = APIRouter(prefix='/posts', tags=['Post API'])


@post_router.get('', response_model=GetPostResponse)
async def all_post(request: Request):
    return post_service.get_posts(request)

@post_router.get('/{id}', response_model=GetPostResponse)
async def post_by_id(request: Request, id: int):
    return post_service.get_post_by_id(request, id)

@post_router.post('', response_model=CreatePostResponse)
async def add_post(request: Request, create_post: CreatePostRequest):
    return post_service.create_posts(request, create_post)

@post_router.put('/{id}', response_model=UpdatePostResponse)
async def update_post(request: Request, id:int, update_post: UpdatePostRequest):
    return post_service.update_post_by_id(request, id, update_post)

@post_router.delete('/{id}', response_model=DeletePostResponse)
async def delete_post(request:Request, id:int):
    return post_service.delete_post_by_id(request, id)