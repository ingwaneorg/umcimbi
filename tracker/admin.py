from django.contrib import admin
from .models import Course, Event, User, Activity, UserActivity

# Register the Course model
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    list_filter = (['code'])
    ordering = (['code']) 
    search_fields = ('code', 'name')

# Register the Event model
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_id', 'short_code', 'course', 'active', 'start_date', 'end_date')
    list_filter = ('active', 'course')
    search_fields = ('event_id', 'course__code', 'short_code')

# Register the User model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'vm_url')
    list_filter = (['user_id'])
    ordering = (['user_id']) 
    search_fields = ('user_id', 'name')

# Register the Activity model
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_id', 'course', 'title', 'day', 'sort_order')
    list_filter = ('course', 'day')
    ordering = ('course','sort_order') 
    search_fields = ('title', 'course__code')

# Register the UserActivity model
@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'activity', 'completed', 'comment')
    list_filter = (['event__event_id'])
    ordering = ('event','user','activity') 
    search_fields = ('activity__title', 'event__short_code')
