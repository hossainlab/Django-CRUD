from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Developer 
from .forms import DeveloperForm

# TODO: CRUD
# CREATE--> New
# RETRIEVE--> Get
# UPDATE--> Edit
# DELETE--> Delete


# HomeView
def index(request): 
    developers = Developer.objects.all()
    form = DeveloperForm()
    context = {
        'developers': developers, 
        'form':form, 
    }
    return render(request, 'myapp/index.html', context)

# InsertView
def addDeveloper(request): 
    if request.method == 'POST': 
        form = DeveloperForm(request.POST or None)
        if form.is_valid(): 
            form.save()
            messages.success(request, f'Your information has been inserted!')
            return redirect('home')

# EditView
def editDeveloper(request,id): 
    select = Developer.objects.get(id=id)
    form = DeveloperForm(request.POST or None, instance=select) 
    if request.method == 'POST':
        if form.is_valid(): 
            dev = form.save(commit=False)
            dev.save()
            messages.success(request, f'Data has been updated!')
            return redirect('home') 
    # return render(request, 'myapp/edit.html',{'form':form})


# DeleteView
def deleteDeveloper(request, id): 
    developer = Developer.objects.get(id=id)
    developer.delete()
    messages.success(request, f'Data has been deleted!')
    return redirect('home')
