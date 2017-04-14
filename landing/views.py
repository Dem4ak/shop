from django.shortcuts import render
from .forms import SubscriberForm

def landing(request):
    form = SubscriberForm(request.POST or None)
    name = "Roma"
    if request.method == "POST" and form.is_valid():
        new_form = form.save()
    return render(request, 'landing/landing.html', locals())
