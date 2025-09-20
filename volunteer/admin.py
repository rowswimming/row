from django.contrib import admin
from volunteer.models import Opportunity
from volunteer.models import Volunteering

# Register your models here.
admin.site.register(Opportunity)
admin.site.register(Volunteering)