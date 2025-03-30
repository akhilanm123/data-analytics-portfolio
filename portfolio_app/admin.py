from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'skills', 'github_link', 'live_demo')  # Show key fields in admin
    search_fields = ('title', 'skills')  # Enable search by title & skills
    list_filter = ('skills',)  # Add a filter for skills in the admin panel


from django.contrib import admin
from .models import Skill  # ✅ Import Skill model

admin.site.register(Skill)  # ✅ Register Skill model

