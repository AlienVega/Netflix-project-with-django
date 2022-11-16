from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import *
# Create your views here.
def userRegister(request):
    if request.method =='POST':
        kullanici = request.POST['kullanici']
        email = request.POST['email']
        sifre1 = request.POST['sifre1']
        sifre2 = request.POST['sifre2']
        resim=request.FILES['resim']
        telefon= request.POST['telefon']
        if kullanici != "" and email != "" and sifre1 != "" and sifre2 != "" :
            if sifre1 == sifre2:
                if User.objects.filter(username=kullanici).exists():
                    messages.error(request,"bu kullanıcı adı zaten mevcut")
                    return redirect("register")
                elif User.objects.filter(email = email).exists():
                    messages.error(request,"bu e-mail kullanımda")
                    return redirect("register")
                elif len(sifre1)<6:
                    messages.error(request,'şifre en az 6 karakter olmalıdır')
                    return redirect("register")
                elif kullanici in sifre1:
                    messages.error(request,"kullanıcı adı ile şifre aynı olmamalıdır")
                    return redirect('register')
                else:
                    user =User.objects.create_user(username=kullanici,email=email,password=sifre1)
                    Hesap.objects.create(
                        user =user,
                        resim=resim,
                        telefon=telefon
                    )
                    messages.success(request,"kullanıcı oluşturuldu")
                    return redirect("index")
            else:
                messages.error(request,"şifreler uyuşmuyor")
                return redirect("register")
        else:
            messages.error(request,"bütün alanların doldurulması zorunludur")
            return redirect("register")
    return render(request,"register.html")

def userLogin(request):
    if request.method == "POST" :
        kullanici = request.POST["kullanici"]
        sifre =request.POST["sifre"]

        user = authenticate(request, username=kullanici, password=sifre)
        if user is not None:
            login(request,user)
            messages.success(request,"Giriş Yapıldı")
            return redirect("profiles")
        else:
            messages.error(request,"kullanıcı adı veya şifre hatalı")
            return redirect("login")
    return render(request,"login.html")

def profiles(request):
    profiller = Profil.objects.filter(olusturan = request.user)
    context ={
        'profiller':profiller
    }
    return render(request,"browse.html",context)
def olustur(request):
    form = ProfilForm()
    if request.method == "POST":
        form =ProfilForm(request.POST,request.FILES)
        if form.is_valid():
            if Profil.objects.filter(olusturan =request.user).count() <4:
                profil = form.save(commit=False)
                profil.olusturan = request.user
                profil.save()
                messages.success(request,"Profil oluşturuldu")
                return redirect("profiles")
            else:
                messages.error(request,"en fazla 4 afet profil oluşturulabilir")
                return redirect("profiles")
    context ={
        "form":form
    }
    return render(request,"olustur.html",context)

def hesap(request):
    profil = request.user.hesap
    context = {
        'profil':profil
    }
    return render(request ,'hesap.html',context) 
def sil(request):
    user=request.user
    user.delete()
    messages.success(request,"kullanıcı silindi")
    return redirect('index')
def update(request):
    # forms.py den yaptığımız zaman
    # form=UserForm(instance = request.user)
    # if request.method=='POST':
    #     form =UserForm(request.POST,instance=request.user)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request,'bilgiler güncellendi')
    #         return redirect('hesap')
    # context ={
    #     'form':form
    # }
    # return render(request,'update.html',context)

    # formu kendimiz yaptığımız zaman

    if request.method == 'POST':
        kullanici=request.POST['kullanici']
        email = request.POST['email']
        user =request.user
    
        user.username=kullanici
        user.email =email
        user.save()
        messages.success(request,'güncellendi')
        return redirect('hesap')

    return render(request,'update.html')

def userLogout(request):
    logout(request)
    messages.success(request,'Çıkış yapıldı')
    return redirect('index')

def ekleme(request):
    return redirect('index')
