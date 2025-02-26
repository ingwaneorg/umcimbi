from django.db import models

class Course(models.Model):
    code = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.code


class Event(models.Model):
    event_id = models.IntegerField(primary_key=True)
    short_code = models.CharField(max_length=4, unique=True)  # base64 version of event_id
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Event {self.event_id} - {self.course.code}"


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    vm_url = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.user_id} - {self.name}"


class Activity(models.Model):
    activity_id = models.IntegerField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    day = models.IntegerField()  # Which day the activity is on
    sort_order = models.IntegerField()

    def __str__(self):
        return f"{self.activity_id} - {self.title}"

    class Meta:
        verbose_name_plural = "Activities"


class UserActivity(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    comment = models.TextField(blank=True, null=True)

    # Unique constraint to prevent duplicate entries for the same user and activity in an event
    class Meta:
        unique_together = ('event', 'user', 'activity')

    def __str__(self):
        return f"{self.user.name} - {self.activity.title} - {'Completed' if self.completed else 'Pending'}"

    class Meta:
        verbose_name_plural = "UserActivities"

