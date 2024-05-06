from django.shortcuts import render, redirect
import httpx
import json
import asyncio
import speech_recognition as sr

def add_book_to_cart(request):
    customer_id = request.session['user']['id']
    cart_id = request.session['cart_id']
    book_id = request.POST.get('book_id')
    quantity = request.POST.get('quantity')
    price = request.POST.get('price')
    data = {
        'book_id': book_id,
        'title': request.POST.get('title'),
        'image': request.POST.get('image'),
        'price': price,
        'total_price': int(quantity) * int(price),
        'quantity': quantity,
        'cart': cart_id,
    }
    async def add_cart():
        async with httpx.AsyncClient() as client:
            response = await client.post('http://localhost:8002/add-book-cart/', data=data)
    response = asyncio.run(add_cart())
    return redirect(f'/book/{book_id}/')

def add_clothes_to_cart(request):
    customer_id = request.session['user']['id']
    cart_id = request.session['cart_id']
    clothes_id = request.POST.get('clothes_id')
    quantity = request.POST.get('quantity')
    price = request.POST.get('price')
    data = {
        'clothes_id': clothes_id,
        'name': request.POST.get('name'),
        'image': request.POST.get('image'),
        'price': price,
        'total_price': int(quantity) * int(price),
        'quantity': quantity,
        'cart': cart_id,
    }
    async def add_cart():
        async with httpx.AsyncClient() as client:
            response = await client.post('http://localhost:8002/add-clothes-cart/', data=data)
    response = asyncio.run(add_cart())
    return redirect(f'/clothes/{clothes_id}/')

def add_mobile_to_cart(request):
    customer_id = request.session['user']['id']
    cart_id = request.session['cart_id']
    mobile_id = request.POST.get('mobile_id')
    quantity = request.POST.get('quantity')
    price = request.POST.get('price')
    data = {
        'mobile_id': mobile_id,
        'name': request.POST.get('name'),
        'image': request.POST.get('image'),
        'price': price,
        'total_price': int(quantity) * int(price),
        'quantity': quantity,
        'cart': cart_id,
    }
    async def add_cart():
        async with httpx.AsyncClient() as client:
            response = await client.post('http://localhost:8002/add-mobile-cart/', data=data)
    response = asyncio.run(add_cart())
    return redirect(f'/mobile/{mobile_id}/')

def get_cart(request):
    customer_id = request.session['user']['id']
    cart = httpx.get(f'http://127.0.0.1:8002/cart-detail/?customer_id={customer_id}').json()
    total_price = 0
    for book in cart['cart_book']:
        total_price += book['total_price']
    for clothes in cart['cart_clothes']:
        total_price += clothes['total_price']
    for mobile in cart['cart_mobile']:
        total_price += mobile['total_price']
    return render(request, 'carts.html', {
        'cart': cart,
        'total_price': total_price,
    })

def get_search_page(request):
    return render(request, 'search/products.html')

def search(request):
    keyword = request.GET.get('query')
    product = request.GET.get('product')
    category_id = int(request.GET.get('category', 0))
    async def get_products():
        async with httpx.AsyncClient() as client:
            response = await client.get(f'http://127.0.0.1:8009/search/?keyword={keyword}')
        return response.json()
    response = asyncio.run(get_products())
    books = response['list_books']
    clothes = response['list_clothes']
    mobiles = response['list_mobiles']
    cart_book = response['cart_book']
    cart_clothes = response['cart_clothes']
    cart_mobile = response['cart_mobile']
    if product == 'book':
        if category_id:
            books = [book for book in books if book['category'] == category_id]
        return render(request, 'search/products.html', {
            'books': books,
            'query': keyword,
            'product': product,
            'cart_book': cart_book,
            'category_id': category_id,
        })
    if product == 'clothes':
        if category_id:
            clothes = [item for item in clothes if item['category'] == category_id]
        return render(request, 'search/products.html', {
            'clothes': clothes,
            'query': keyword,
            'product': product,
            'cart_clothes': cart_clothes,
            'category_id': category_id,
        })
    if product == 'mobile':
        if category_id:
            mobiles = [mobile for mobile in mobiles if mobile['category'] == category_id]
        return render(request, 'search/products.html', {
            'mobiles': mobiles,
            'query': keyword,
            'product': product,
            'cart_mobile': cart_mobile,
            'category_id': category_id,
        })
    return render(request, 'search/products.html', {
        'books': books,
        'clothes': clothes,
        'mobiles': mobiles,
        'query': keyword,
        'product': product,
    })

def search_voice(request):
    recognizer = sr.Recognizer()
    
    query = ''

    with sr.Microphone() as source:
        print("Đang nghe... (nói 'kết thúc' để dừng lại)")

        try:
            # Tự động điều chỉnh nền để loại bỏ tiếng ồn
            recognizer.adjust_for_ambient_noise(source)
            
            audio_data = recognizer.listen(source, timeout=3)
            print("Đã nghe xong. Đang nhận dạng...")

            query = recognizer.recognize_google(audio_data, language="vi-VN")
            print("Văn bản nhận dạng từ giọng nói: {}".format(query))

        except sr.UnknownValueError:
            print("Không thể nhận dạng giọng nói")
        except sr.RequestError as e:
            print("Lỗi khi gửi yêu cầu đến API Google: {}".format(e))
        except sr.WaitTimeoutError:
            print("Hết thời gian chờ. Không có âm thanh được nghe.")

    # Kiểm tra nếu text là None hoặc trống thì gán giá trị khoảng trắng
    keyword = query or ''
    async def get_products():
        async with httpx.AsyncClient() as client:
            response = await client.get(f'http://127.0.0.1:8009/search/?keyword={keyword}')
        return response.json()
    response = asyncio.run(get_products())
    books = response['list_books']
    clothes = response['list_clothes']
    mobiles = response['list_mobiles']
    return render(request, 'search/products.html', {
        'books': books,
        'clothes': clothes,
        'mobiles': mobiles,
        'query': keyword,
    })

def order_form(request):
    cart = request.POST.get('cart')
    total_price = int(request.POST.get('total_price'))
    cart = cart.replace("'", "\"")
    cart = json.loads(cart)
    return render(request, 'order.html', {
        'cart': cart,
        'total_price': total_price,
    })

def add_order(request):
    username = request.session['user']['name']
    customer_id = request.session['user']['id']
    if request.POST.get('mobile'):
        mobile = request.POST.get('mobile')
    else:
        mobile = request.session['user']['mobile']
    if request.POST.get('delivery_address'):
        delivery_address = request.POST.get('delivery_address')
    else:
        delivery_address = request.session['user']['delivery_address']
    total_price = request.POST.get('total_price')
    data = {
        'username': username,
        'customer_id': customer_id,
        'mobile': mobile,
        'delivery_address': delivery_address,
        'total_price': total_price,
    }
    print(data)
    async def create_order():
        async with httpx.AsyncClient() as client:
            response = await client.post('http://127.0.0.1:8003/add-order/', data=data)
    response = asyncio.run(create_order())
    print(request.session['user'])
    return render(request, 'success.html')

def get_list_order(request):
    customer_id = request.session['user']['id']
    data = {'customer_id': customer_id}
    list_order = httpx.get(f'http://127.0.0.1:8003/list-order/?customer_id={customer_id}').json()
    return render(request, 'order/ds-order.html', {
        'ds_order': list_order
    })

def detail_order(request, order_id):
    async def get_response():
        async with httpx.AsyncClient() as client:
            order = await client.get(f'http://127.0.0.1:8003/detail-order/?order_id={order_id}')
            shipment_status = await client.get(f'http://127.0.0.1:8006/shipment-status/?order_id={order_id}')
            return order.json(), shipment_status.json()
    order, shipment_status = asyncio.run(get_response())
    return render(request, 'order/detail-order.html', {
        'order': order,
        'shipment_status': shipment_status,
    })

def cancel_order(request):
    order_id = request.POST.get('order_id')
    response = httpx.delete(f'http://127.0.0.1:8003/order/{order_id}/')
    return redirect('/list-order/')