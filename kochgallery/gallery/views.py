from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import models

# Create your views here.


class ImageForm(forms.ModelForm):
    """Klasse zur Formularerstellung."""
    class Meta:
        model = models.Image
        exclude = []

def overview(request):
    all_images = models.Image.objects.all()
    return render(request, 'index.html', dict(images=all_images))




def upload(request):
    # werden Formulardaten geschickt?
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():  # Formular überprüfen
            form.save()
            return HttpResponseRedirect('/')  # Umleitung
    else:
        form = ImageForm()  # leeres Formular
    return render(request, 'upload.html', dict(form=form))