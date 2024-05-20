from django.shortcuts import render
from django.http import HttpResponse
from .models import books
from .serializers import BookSerializer
  

def list_books(request):
    books2 = books.objects.all()
    serializer = BookSerializer(books2, many=True)
    return render(request, 'readings/listar_books.html', {'books': serializer.data})

def create_books(request):
    if request.method == "POST":
        serializer = BookSerializer(data=request.POST)
        if serializer.is_valid():
           serializer.save()
           #return redirect('list')
    else:
        serializer = BookSerializer()

    return render(request, 'readings/create_books.html', {'form': serializer})
