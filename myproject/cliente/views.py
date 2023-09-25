from django.shortcuts import render
from django.shortcuts import redirect



from . import models
from . import forms


# Create your views here.

def index(request):
    clientes = models.Cliente.objects.all()    
    return render(request, "cliente/index.html",{"clientes":clientes})

def crear(request):   
    if request.method == "POST":
        form = forms.ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:index")
    else:
        form = forms.ClienteForm()
    return render(request, "cliente/crear.html",{"form": form})
        
        
    



