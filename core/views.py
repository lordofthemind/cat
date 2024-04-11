from django.shortcuts import render, redirect
from .forms import CreateUserForm

# Create your views here.
from django.http import HttpResponse


def coreindex(request):
    return HttpResponse('Hello, index page for app core is ready.')

def createUserView(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('coreindex')
        
    else:
        form = CreateUserForm
        return render(request, 'core/create_user.html', {'form':form})
