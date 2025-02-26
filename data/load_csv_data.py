import csv
import os
import django

# Setup Django environment (Only needed if running as standalone script)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "event.settings")
django.setup()

from tracker.models import Course, User, Activity, Event, UserActivity

def load_courses(csv_file_path):
    """Load course data from CSV file."""
    with open(csv_file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Course.objects.create(
                code=row['code'],  
                name=row['name']
            )
    print("Courses loaded successfully!")


def load_users(csv_file_path):
    """Load or update course data from a CSV file."""
    with open(csv_file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user, created = User.objects.update_or_create(
                user_id=row['user_id'],
                defaults={'name': row['name'],'vm_url': row['vm_url']}
            )
            if created:
                print(f"Created new user: {user.user_id}")
            else:
                print(f"Updated existing user: {user.user_id}")
    
    print("Users loaded/updated successfully!")


def load_activities(csv_file_path):
    """Load or update course data from a CSV file."""
    with open(csv_file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            course_instance = Course.objects.get(code=row['course'])
            activity, created = Activity.objects.update_or_create(
                activity_id=row['activity_id'],
                defaults={
                    'course': course_instance,
                    'day': row['day'],
                    'sort_order': row['sort_order'],
                    'title': row['title']
                    }
            )
            if created:
                print(f"Created new activity: {activity.activity_id}")
            else:
                print(f"Updated existing activity: {activity.activity_id}")
    
    print("Courses loaded/updated successfully!")

def user_activities(event_id):
    # Fetch existing records
    event_instance = Event.objects.get(event_id=event_id)
    activity_instance = Activity.objects.get(activity_id=0)

    for i in range(1,21):
        user_instance = User.objects.get(user_id=i)
        user_activity, created = UserActivity.objects.update_or_create(
            event=event_instance,
            user=user_instance,
            activity=activity_instance,
            completed=False,
            comment=""
        )
        if created:
            print(f"Created new user activity: {user_activity.user_id}")
        else:
            print(f"Updated existing user activity: {user_activity.user_id}")


    
    print("User/Activities loaded/updated successfully!")




if __name__ == "__main__":
    # Adjust paths if needed
    course_csv = "data/courses.csv"
    user_csv = "data/users.csv"
    activity_csv = "data/activity.csv"

    #load_courses(course_csv)
    #load_users(user_csv)
    #load_activities(activity_csv)

    event_id = 4836924
    user_activities(event_id)