from django.db import models


class ShortURL(models.Model):
    """Stores the mapping between original URLs and generated short codes."""
    original_url = models.URLField(max_length=2048, help_text="The destination URL to shorten")
    short_code = models.CharField(max_length=6, unique=True, db_index=True, help_text="Unique 6-character identifier")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Short URL"
        verbose_name_plural = "Short URLs"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"
