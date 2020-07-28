from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from books.models import Book, Publish, Author


# Create your views here.
def books(request):
    book_list = Book.objects.all()

    return render(request, 'books.html', locals())


def add(request):
    if request.method=='GET':

        publish_list = Publish.objects.all()
        author_list = Author.objects.all()

        return render(request, 'addbook.html', locals())
    else:
        title=request.POST.get('title')
        price = request.POST.get('price')
        publish_id = request.POST.get('publish_id')
        pub_date = request.POST.get('pub_date')
        authors = request.POST.getlist('authors')

        book=Book.objects.create(title=title,price=price,publish_id=publish_id,pub_date=pub_date)
        book.authors.add(*authors)

        return redirect(reverse('books'))


def delbook(request, delete_book_id):
    Book.objects.filter(pk=delete_book_id).delete()

    return redirect(reverse('books'))


def edit(request, edit_book_id):
    edit_book = Book.objects.filter(pk=edit_book_id).first()
    if request.method == 'GET':

        publish_list = Publish.objects.all()
        author_list = Author.objects.all()
        return render(request, 'editbook.html', locals())
    else:
        title = request.POST.get('title')
        price = request.POST.get('price')
        publish_id = request.POST.get('publish_id')
        pub_date = request.POST.get('pub_date')
        authors= request.POST.getlist('authors')
        Book.objects.filter(pk=edit_book_id).update(title=title,
                                                    price=price,
                                                    publish_id=publish_id,
                                                    pub_date=pub_date,
                                                    )
        edit_book.authors.set(authors)
        return redirect(reverse('books'))
