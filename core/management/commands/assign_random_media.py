import os
import random
from django.core.management.base import BaseCommand
from core.models import Movie
from django.conf import settings

class Command(BaseCommand):
    help = 'Assign random images and videos from media folders to each movie.'

    def handle(self, *args, **options):
        image_dir = os.path.join(settings.MEDIA_ROOT, 'movie_images')
        video_dir = os.path.join(settings.MEDIA_ROOT, 'movie_videos')
        image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
        video_files = [f for f in os.listdir(video_dir) if os.path.isfile(os.path.join(video_dir, f))]

        if not image_files or not video_files:
            self.stdout.write(self.style.ERROR('No images or videos found in media folders.'))
            return

        movies = Movie.objects.all()
        for movie in movies:
            img = random.choice(image_files)
            vid = random.choice(video_files)
            movie.image_card.name = f'movie_images/{img}'
            movie.image_cover.name = f'movie_images/{img}'
            movie.video.name = f'movie_videos/{vid}'
            movie.save()
            self.stdout.write(self.style.SUCCESS(f'Updated {movie.title} with {img} and {vid}'))
        self.stdout.write(self.style.SUCCESS('All movies updated.'))
