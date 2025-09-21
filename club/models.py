from django.conf import settings
from django.db import models


class Parent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        print(self.user.last_name)

        name = ''
        if self.user.first_name:
            name = name + self.user.first_name
        if self.user.last_name:
            name = name + ' ' + self.user.last_name
        if not name:
            name = self.user.username

        return name
