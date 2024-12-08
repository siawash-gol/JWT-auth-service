from django.db import models
from config.auth.Users.models import User
from config.auth.Profiles.cities_list import StateChoices, CitiesChoices


class Profile(models.Model):
    class LanguageChoices(models.TextChoices):
        en = 'en', 'English'
        fa = 'fa', 'persian'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    language = models.CharField(max_length=64,
                                choices=LanguageChoices.choices,
                                default=LanguageChoices.en,
                                null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)

    state = models.CharField(max_length=150, null=True, blank=True, choices=StateChoices.choices)

    city = models.CharField(max_length=150, null=True, blank=True, choices=CitiesChoices.choices)

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return self.username


class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'
