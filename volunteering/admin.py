from django.contrib import admin
from volunteering.models import Opportunity, OpportunityAdmin, VolunteerAdmin
from volunteering.models import Volunteer

# Register your models here.
admin.site.register(Opportunity, OpportunityAdmin)
admin.site.register(Volunteer, VolunteerAdmin)