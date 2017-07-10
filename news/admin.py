from django.contrib import admin

from .models import NewsData, Activity, Reference, Team, Partners, Contacts

admin.site.register(NewsData)
admin.site.register(Activity)
admin.site.register(Reference)
admin.site.register(Team)
admin.site.register(Partners)
admin.site.register(Contacts)
