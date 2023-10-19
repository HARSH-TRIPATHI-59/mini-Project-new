from django.contrib import admin
from .models import Profile
from .models import Video
from .models import Contact
from .models import Dealer

# Register your models here.
admin.site.register(Profile)
admin.site.register(Video)
admin.site.register(Contact)
admin.site.register(Dealer)
