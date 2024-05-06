import httpx
import asyncio
from rest_framework import status
from django.http import HttpResponse
import json

def search_keyword(request):
    keyword = request.GET['keyword']
    
    async def fetch_data(url):
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            return response.json()
    async def get_response():
        books_task = asyncio.create_task(fetch_data(f'http://localhost:8008/book/?search={keyword}'))
        clothes_task = asyncio.create_task(fetch_data(f'http://localhost:8008/clothes/?search={keyword}'))
        mobiles_task = asyncio.create_task(fetch_data(f'http://localhost:8008/mobile/?search={keyword}'))
        cart_book_task = asyncio.create_task(fetch_data('http://localhost:8008/category-book/'))
        cart_clothes_task = asyncio.create_task(fetch_data('http://localhost:8008/category-clothes/'))
        cart_mobile_task = asyncio.create_task(fetch_data('http://localhost:8008/category-mobile/'))
        list_books = await books_task
        list_clothes = await clothes_task
        list_mobiles = await mobiles_task
        cart_book = await cart_book_task
        cart_clothes = await cart_clothes_task
        cart_mobile = await cart_mobile_task
        return {
            'list_books': list_books,
            'list_clothes': list_clothes,
            'list_mobiles': list_mobiles,
            'cart_book': cart_book,
            'cart_clothes':cart_clothes,
            'cart_mobile': cart_mobile,
        }
    
    response = asyncio.run(get_response())
    return HttpResponse(json.dumps(response), status=status.HTTP_200_OK, content_type = 'application/json')