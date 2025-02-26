from django.shortcuts import render, get_object_or_404
from .models import Event, User, UserActivity

def event_users(request, short_code):
    # Get event using the short code
    event = get_object_or_404(Event, short_code=short_code)

    # Get users associated with the event
    users = User.objects.filter(useractivity__event=event).distinct()

    context = {
        'event': event,
        'users': users,
    }
    return render(request, 'event_users.html', context)


def user_progress(request, short_code, user_id):
    # Get event using the short code
    event = get_object_or_404(Event, short_code=short_code)

    # Get user
    user = get_object_or_404(User, user_id=user_id)

    # Get all activities for this user in this event
    user_activities = UserActivity.objects.filter(event=event, user=user).select_related('activity').order_by('activity__day', 'activity__sort_order')

    context = {
        'event': event,
        'user': user,
        'user_activities': user_activities,
    }
    return render(request, 'user_progress.html', context)
