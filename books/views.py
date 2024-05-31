from django.shortcuts import render

# Create your views here.
def books(request):
    return render(request, "main.html")

def authorDetail(request):
    return render(request, "author_detail.html")

def authorList(request):
    return render(request, "author_list.html")

def bookDetail(request):
    return render(request, "book_detail.html")

def bookList(request):
    return render(request, "book_list.html")

def bookListOrdered(request):
    return render(request, "book_list_ordered.html")