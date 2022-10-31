from django.shortcuts import HttpResponse, render
from .models import Book
# Create your views here.
def index(request):
    return HttpResponse('Hello, world!')

def book_by_id(request,book_id):
    book = Book.objects.get(pk=book_id)
#    return HttpResponse(f'Book:{book.title}, publish on {book.pub_date}')
    return render(request,'my_app/book_details.html',{'book':book})