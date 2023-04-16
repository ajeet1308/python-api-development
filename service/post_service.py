from fastapi import Request
from random import randrange
from schema.response import GetPostResponse, UpdatePostResponse, CreatePostResponse, DeletePostResponse
from schema.request import CreatePostRequest, UpdatePostRequest
    
    
my_posts = [{"title": "title of post 1", "content": "content of post1", "id":1},
            {"title": "title of post2", "content": "content of post2", "id":2}]

########################################
def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i
#########################################


def get_posts(request: Request):
    try:
        return GetPostResponse(**{'message':'success', 'data':my_posts})
    except Exception as exc:
        return {'message': exc}



def create_posts(request: Request, obj: CreatePostRequest):
    try:
        body_dict = obj.dict()
        body_dict['id'] = randrange(1,1000000)
        my_posts.append(body_dict)
        return CreatePostResponse(**{'message': 'success', 'id': body_dict['id']})
    except Exception as exc:
        return {'message': exc}


def get_post_by_id(request: Request, id: int):
    try:
        post = find_post(id)
        if not post:
            return GetPostResponse(**{'message':'No post with such id exists', 'data': []})
        return GetPostResponse(**{'message':'success', 'data': [post]})
    except Exception as exc:
        return {'message':exc}


def delete_post_by_id(request:Request, id:int):
    try:
        #deleting post
        #find the index in the array of required id
        # my_post.pop(index)
        index = find_index_post(id)
        if index == None:
            return DeletePostResponse(**{'message':'No post with such id exists'})
        my_posts.pop(index)
        return DeletePostResponse(**{'message':'success'})
    except Exception as exc:
        return {'message':exc}


def update_post_by_id(request: Request, id:int, obj: UpdatePostRequest):
    try:
        index = find_index_post(id)
        if index == None:
            return UpdatePostResponse(**{'message':'No post with such id exists', 'id': id})
        body_dict = obj.dict()
        body_dict['id'] = id
        my_posts[index] = body_dict
        return UpdatePostResponse(**{'message':'success', 'id': id})
    except Exception as exc:
        return {'message':exc}