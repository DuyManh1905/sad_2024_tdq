from django.shortcuts import render, redirect
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.sessions import middleware
import httpx
import asyncio
import json
from django.conf import settings

def get_home(request):
    async def get_products():
        async with httpx.AsyncClient() as client:
            books = await client.get('http://127.0.0.1:8008/books/')
            clothes = await client.get('http://127.0.0.1:8008/clothes-all/')
            mobiles = await client.get('http://127.0.0.1:8008/mobiles/')
        return books.json(), clothes.json(), mobiles.json()
    books, clothes, mobiles = asyncio.run(get_products())
    return render(request, 'index.html', {
        'books': books,
        'clothes': clothes,
        'mobiles': mobiles,
    })

def login_form(request):
    return render(request, 'login.html')

def check_login(request):
    mobile = request.POST.get('mobile')
    password = request.POST.get('password')
    data = {
        'mobile': mobile,
        'password': password,
    }
    async def get_user():
        async with httpx.AsyncClient() as client:
            response = await client.post('http://localhost:8001/check-user/', data=data)
        return response
    response = asyncio.run(get_user())
    print(response.json())
    if response.status_code == 200:
        if response.json()['role'] == 'customer':
            customer_id = response.json()['id']
            cart_id = httpx.get(f'http://127.0.0.1:8002/cart_id/?customer_id={customer_id}').json()['cart_id']
            request.session['cart_id'] = cart_id
            request.session.set_expiry(settings.SESSION_COOKIE_AGE)
        request.session['user'] = response.json()
        print(request.session['user'])
        return redirect('/')
    else:
        return render(request, 'login.html', {
            'error_message': response.json()['message'],
        })

def logout(request):
    request.session.clear()
    return redirect('/')

def detail_book(request, book_id):
    data = {'id', book_id}
    book = httpx.get(f'http://127.0.0.1:8008/detail/book/?id={book_id}').json()
    print(book)
    return render(request, 'book/detail.html', {
        'book': book,
    })
    
def detail_clothes(request, clothes_id):
    data = {'id', clothes_id}
    clothes = httpx.get(f'http://127.0.0.1:8008/detail/clothes/?id={clothes_id}').json()
    print(clothes)
    return render(request, 'clothes/detail.html', {
        'clothes': clothes,
    })
    
def detail_mobile(request, mobile_id):
    data = {'id', mobile_id}
    mobile = httpx.get(f'http://127.0.0.1:8008/detail/mobile/?id={mobile_id}').json()
    print(mobile)
    return render(request, 'mobile/detail.html', {
        'mobile': mobile,
    })