from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import UserInput

def form_view(request):
    if request.method == "POST":
        form_dict = dict(request.POST)
        form_dict.pop('csrfmiddlewaretoken', None)
        polished_data={k: v[0] for k, v in form_dict.items()}
        UserInput.objects.create(inputedData=polished_data)
        return redirect('display_view')
    return render(request, 'form.html')

def display_view(request):
    allData=UserInput.objects.all().order_by('-creationDate')
    return render(request, 'display.html', {'allData': allData})

@require_POST
def wipe_view(request):
    UserInput.objects.all().delete()
    return redirect('display_view')