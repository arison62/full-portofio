from django.contrib import admin

from .models import Education, Experience, Profile, Project, Skill, SocialLink



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'is_public', 'is_active')
    search_fields = ('title', )
    list_filter = ('is_public', 'is_active')
    readonly_fields = ('slug',)

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('profile', 'name', 'platform')
    search_fields = ('profile__user__username', 'name')
    list_filter = ('platform',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('profile', 'name', 'project_type', 'status')
    search_fields = ('profile__user__username', 'name')
    list_filter = ('project_type', 'status')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('profile', 'title', 'company', 'start_date', 'end_date', 'is_current')
    search_fields = ('profile__user__username', 'title', 'company')
    list_filter = ('is_current',)
    date_hierarchy = 'start_date'

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('profile', 'degree', 'institution', 'start_date', 'end_date', 'is_current')
    search_fields = ('profile__user__username', 'degree', 'institution')
    list_filter = ('is_current',)
    date_hierarchy = 'start_date'

