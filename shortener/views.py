import random
import string
from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortURL


def generate_code(length: int = 6) -> str:
    """Generates a random alphanumeric short code."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))


def home(request):
    """Renders the homepage and handles URL shortening form submissions."""
    short_url = None

    if request.method == 'POST':
        original_url = request.POST.get('url', '').strip()

        if original_url:
            code = generate_code()
            while ShortURL.objects.filter(short_code=code).exists():
                code = generate_code()

            obj = ShortURL.objects.create(
                original_url=original_url,
                short_code=code
            )

            short_url = request.build_absolute_uri('/') + obj.short_code

    return render(request, 'home.html', {
        'short_url': short_url
    })


def redirect_url(request, code):
    """Redirects the short code to the corresponding destination URL."""
    short_url_obj = get_object_or_404(ShortURL, short_code=code)
    return redirect(short_url_obj.original_url)
