from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from books.models import Book


# Create your views here.

def add(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        price = request.POST.get("price")
        pub_date = request.POST.get("pub_date")
        publish = request.POST.get("publish")
        book = Book.objects.create(title=title,
                                   price=price,
                                   pub_date=pub_date,
                                   publish=publish)
        return redirect(reverse("books"))
    else:

        return render(request, 'addbook.html')


def books(request):
    book_list = Book.objects.all()

    return render(request, 'books.html', locals())


def delbook(request, delete_book_id):
    Book.objects.filter(nid=delete_book_id).delete()

    return redirect(reverse('books'))


def edit(request, edit_book_id):
    if request.method == 'GET':
        edit_book = Book.objects.filter(nid=edit_book_id)[0]
        return render(request, 'editbook.html', locals())
    else:
        title = request.POST.get('title')
        price = request.POST.get('price')
        publish = request.POST.get('publish')
        pub_date = request.POST.get('pub_date')
        Book.objects.filter(nid=edit_book_id).update(title=title,
                                                     price=price,
                                                     publish=publish,
                                                     pub_date=pub_date)
        return redirect(reverse('books'))
