from django.contrib import admin

# Register your models here.
from .models import User, Game, Point, Shot

admin.site.register(User)
admin.site.register(Game)
admin.site.register(Point)
admin.site.register(Shot)

