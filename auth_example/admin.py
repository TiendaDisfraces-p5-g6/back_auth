from django.contrib  import admin
from .models.user    import User
from .models.account import Account
from .models.prenda  import Prenda


# Register your models here.
admin.site.register(User)
admin.site.register(Account)
admin.site.register(Prenda)