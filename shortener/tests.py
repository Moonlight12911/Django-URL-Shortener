from django.test import TestCase
from django.urls import reverse
from .models import ShortURL
from .views import generate_code


class ShortenerUtilsTestCase(TestCase):
    def test_generate_code_length(self):
        code = generate_code()
        self.assertEqual(len(code), 6)

    def test_generate_code_custom_length(self):
        code = generate_code(length=10)
        self.assertEqual(len(code), 10)

    def test_generate_code_alphanumeric(self):
        code = generate_code()
        self.assertTrue(code.isalnum())


class ShortURLModelTestCase(TestCase):
    def test_create_short_url(self):
        url_obj = ShortURL.objects.create(
            original_url="https://www.djangoproject.com/",
            short_code="dj1234"
        )
        self.assertEqual(url_obj.original_url, "https://www.djangoproject.com/")
        self.assertEqual(url_obj.short_code, "dj1234")
        self.assertIn("dj1234", str(url_obj))


class ShortURLViewsTestCase(TestCase):
    def test_home_page_get(self):
        response = self.client.get(reverse('shortener:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_shorten_url_post(self):
        target_url = "https://docs.djangoproject.com/en/stable/"
        response = self.client.post(reverse('shortener:home'), {'url': target_url})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(ShortURL.objects.filter(original_url=target_url).exists())
        self.assertIn('short_url', response.context)
        self.assertIsNotNone(response.context['short_url'])

    def test_redirect_to_original_url(self):
        target_url = "https://python.org/"
        obj = ShortURL.objects.create(original_url=target_url, short_code="py0001")
        response = self.client.get(reverse('shortener:redirect_url', kwargs={'code': obj.short_code}))
        self.assertRedirects(response, target_url, fetch_redirect_response=False)

    def test_redirect_non_existent_code_returns_404(self):
        response = self.client.get(reverse('shortener:redirect_url', kwargs={'code': 'nonexist'}))
        self.assertEqual(response.status_code, 404)
