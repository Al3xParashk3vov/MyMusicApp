from django.core.validators import MinValueValidator
from django.db import models

from albums.choices import GenreChoices


class Album(models.Model):
    album_name = models.CharField(
        max_length=30,
        unique=True,
    )

    artist = models.CharField(
        max_length=30,
    )

    genre = models.CharField(
        max_length=30,
        choices=GenreChoices.choices,
    ) # if choice == GenreChoices.OTHER

    description = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField()

    price = models.FloatField( # DecimalField - better
        validators=[
            MinValueValidator(0.0),
        ]
    )
    # Profile.albums or Profile.album_set
    owner = models.ForeignKey(
        to='profiles.Profile',
        on_delete=models.CASCADE,
        related_name='albums',
    )
