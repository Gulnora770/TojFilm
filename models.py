from django.db import models
import uuid
from django.conf import settings

# Create your models here.
class Movie(models.Model):

    GENRE_CHOICES = [
        ('боевик', 'Боевик'),
        ('комедия', 'Комедия'),
        ('драма', 'Драма'),
        ('ужасы', 'Ужасы'),
        ('романтика', 'Романтика'),
        ('научная_фантастика', 'Научная фантастика'),
        ('фэнтези', 'Фэнтези'),
    ]


    uu_id = models.UUIDField(default=uuid.uuid4,editable=False,db_index=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    length = models.PositiveIntegerField()
    image_card = models.ImageField(upload_to='media/movie_images/')
    image_cover = models.ImageField(upload_to='media/movie_images/')

    video = models.FileField(
            upload_to='movie_videos/',
            default='movie_videos/movie_clip.mp4',
            blank=True
        )

    movie_views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
class MovieList(models.Model):
    owner_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)