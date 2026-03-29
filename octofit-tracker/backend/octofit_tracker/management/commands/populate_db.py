from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User.objects.create(email='captainamerica@marvel.com', name='Captain America', team='marvel'),
            User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team='marvel'),
            User.objects.create(email='batman@dc.com', name='Batman', team='dc'),
            User.objects.create(email='superman@dc.com', name='Superman', team='dc'),
            User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team='dc'),
        ]

        # Activities
        Activity.objects.create(user='ironman@marvel.com', activity_type='run', duration=30, date=date(2023, 1, 1))
        Activity.objects.create(user='batman@dc.com', activity_type='cycle', duration=45, date=date(2023, 1, 2))
        Activity.objects.create(user='spiderman@marvel.com', activity_type='swim', duration=25, date=date(2023, 1, 3))
        Activity.objects.create(user='superman@dc.com', activity_type='run', duration=60, date=date(2023, 1, 4))

        # Leaderboard
        Leaderboard.objects.create(team='marvel', points=150)
        Leaderboard.objects.create(team='dc', points=170)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        Workout.objects.create(name='Plank', description='Hold plank for 1 minute', difficulty='medium')
        Workout.objects.create(name='Burpees', description='Do 15 burpees', difficulty='hard')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
