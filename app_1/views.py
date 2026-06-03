from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import UserInput

def form_page(request):
    return render(request, 'form.html')
