from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.core.mail import send_mail
from .forms import FormPost
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'blog/pages/index.html')

def showAll(request):
    return HttpResponse('Aqui estan todos los Posts')

def showOne(request, id):
    return HttpResponse('se ingreso el id ' + id)


def contact(request):
    return HttpResponse('contact form')

def createPost(request):
    form = FormPost()

    if request.method == "POST":
        form = FormPost(request.POST, request.FILES)

        if form.is_valid():
            post = form.save() # aqui era form.save..... deje el post = form.save() para poder hacer post.pk despues
            return redirect('showOne', id=post.pk) # aqui era id, no pk

    return render(request, 'blog/pages/crear_post.html', {'form':form}) # aqui modifique la direccion del template y lo meti dentro de la carpeta pages


def enviarSugerencia(request):
    if request.method == "POST" :

        if len(request.POST['mensaje']) != 0 :
            message = request.POST['mensaje']

            if request.user.is_authenticated :
                message = message + "<br>" + "Sugerencia hecha por: " + request.user.username

            send_mail('Sugerencias', 'Una nueva sugerencia', 'probandoelblogcomp@gmail.com', ['probandoelblogcomp@gmail.com'], html_message = message)
        return  redirect('/')
    else:
        return Http404("Page not found")
