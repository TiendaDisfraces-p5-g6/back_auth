from django.db import models
from .user     import User

class Account(models.Model):
    id                    = models.AutoField(primary_key=True)
    user                  = models.ForeignKey(User, related_name="account", on_delete=models.CASCADE)
    prendasAlquiladas     = models.IntegerField(default=0)
    fechaUltimoAlquiler   = models.DateTimeField(auto_now_add=True)