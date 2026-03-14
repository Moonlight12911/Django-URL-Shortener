# from django.shortcuts import render

# # Create your views here.
from django.shortcuts import render, redirect
from .models import ShortURL
from .utils import generate_code

def home(request):
    short_url = None

    if request.method == 'POST':
        original_url = request.POST.get('url')

        if original_url:
            code = generate_code()
            while ShortURL.objects.filter(short_code=code).exists():
                code = generate_code()

            obj = ShortURL.objects.create(
                original_url=original_url,
                short_code=code
            )

            short_url = request.build_absolute_uri('/') + obj.short_code

    return render(request, 'shortener/home.html', {
        'short_url': short_url
    })



def redirect_url(request, code):
    obj = ShortURL.objects.get(short_code=code)
    return redirect(obj.original_url)
