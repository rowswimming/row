from django.contrib import admin
from volunteering.models import Opportunity
from volunteering.models import Volunteer

# Register your models here.
admin.site.register(Opportunity)
admin.site.register(Volunteer)