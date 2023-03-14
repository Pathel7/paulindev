from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from . form import UserForm


def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            form = UserForm()
    else:
        form = UserForm()

    context = {
        'form': form
    }
    return render(request, 'mainapp/index.html', context)
