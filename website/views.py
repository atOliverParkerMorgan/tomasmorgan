from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from tomasmorgan import settings
from website.models import *


def index(request):
    template = loader.get_template('./index.html')

    about_me = AboutMe.objects.all()[0]
    # songs = Songs.objects.all()[0]
    contact = Contact.objects.all()[0]

    background_images = BackgroundImages.objects.all()[0]

    subtitles_array = []
    for text in about_me.text.all():
        subtitles_array.append(text)

    background_images_array = []
    for image in background_images.background_image.all():
        background_images_array.append(image)

    context = {
        'title': str(about_me.title),
        'subtitles': subtitles_array,
        'subtitles_length': len(subtitles_array),
        'description': str(about_me.description),
        'contact': contact,
        'background_images': background_images_array,
    }
    return HttpResponse(template.render(context, request))
