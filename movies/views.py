from django.shortcuts import render,redirect
from .models import*
from user.models import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def movies(request, slug,id):
    profil =Profil.objects.filter(slug=slug).get(id=id)
    filmler =Movie.objects.all()
    populer = Movie.objects.filter(Kategori__isim ="popüler")
    gundem = Movie.objects.filter(Kategori__isim ="gündemde")
    profiller =Profil.objects.filter(olusturan=request.user)
    context = {
        'filmler':filmler,
        'populer':populer,
        'gundem' :gundem,
        'profil' :profil,
        'profiller':profiller
    }
    return render (request, "browse-index.html",context)
def view_404(request,exception):
    return redirect('/')