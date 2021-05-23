from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .forms import article_form,register_form
from .models import  *

def home(request):
    return render(request,"home.html")

def register(request):
    if request.method=='POST':
        form = register_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password1 = form.cleaned_data.get("password")
            password2 = form.cleaned_data.get("confirm_password")

            if password1==password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Username taken')
                    print("user exits")
                    return redirect('register')
                else:
                    try:
                        validate_password(password1)
                    except ValidationError as e:
                        for i in e:
                            messages.info(request,i) # to be displayed with the field's errors
                        return redirect('register')
                    user=User.objects.create_user(username=username,password=password1)
                    user.save()
                    messages.info(request,'user saved ')
                    return redirect('login')
            else:
                messages.info(request,'Passwords do not match')
                return redirect('register')
    else:
        form = register_form()

    return  render( request,"register.html",{'form':form})

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user= auth.authenticate(username=username, password=password)
        print(user)
        try:
            auth.login(request,user)
            return redirect('/web_page')
        except:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
def web_page(request):
    user_articles = Create_article.objects.filter(username=request.user.username)
    print(user_articles)
    if request.method=='POST':
        username=request.POST['username']
        public_articles = Create_article.objects.filter(private='False', username=username)
        print(len(public_articles))
        return render(request, 'web_page.html',{'flag':0,'username': username, 'public_articles': public_articles, 'user_articles': user_articles})
    return render(request,'web_page.html',{'user_articles':user_articles,'flag':1})

def create_article(request):
    if request.method == 'POST':
        description = request.POST['description']
        image = request.POST['image']
        try:
            private = request.POST['private']
            private = True
        except:
            private = False
        # print(name)
        ins = Create_article(username=request.user.username, description=description, image=image, private=private)
        ins.save()
        messages.info(request, 'article saved')
        print('saved')
    return render(request, 'create_article.html')

