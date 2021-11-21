from django.contrib  import admin
from .models.user    import User
from .models.prenda  import Prenda


# Register your models here.
admin.site.register(User)
admin.site.register(Prenda)