from django.db import models
from django.contrib.auth import get_user_model


class Advert(models.Model):

    CATEGORY_CHOICE = [
        ('ad', 'ad'),
        ('announcement', 'announcement'),
    ]

    title = models.CharField(max_length=250, blank=False, null=False)
    category = models.CharField(max_length=13, choices=CATEGORY_CHOICE, blank=False, null=False)
    description = models.TextField(max_length=400, blank=False, null=False)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    author = models.ForeignKey(get_user_model(), blank=False, null=False, related_name='advert', on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    post_date = models.DateTimeField(auto_now=True)
    moderated = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}: {self.author}'

    class Meta:
        permissions = [
            ('сan_approve', 'Can approve')
        ]