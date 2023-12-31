from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Service(models.Model):
    title = models.CharField(max_length=150)
    class_name = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField()

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title


class Image(models.Model):
    img = models.ImageField(upload_to='pics')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)


class ShoppingCart(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_at = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.service.title} from {self.user.username}'
