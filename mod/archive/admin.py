from django.contrib import admin
from .models import Contracts, Acts, Companies, WorkStage

class CompanyAdmin(admin.ModelAdmin):
    list_display = ("title", "inn")
    prepopulated_fields = {"slug": ["title"]}

admin.site.register(Contracts)
admin.site.register(Acts)
admin.site.register(Companies, CompanyAdmin)
admin.site.register(WorkStage)