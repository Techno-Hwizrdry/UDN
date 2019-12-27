from django.db import models

class Participant(models.Model):
    # Use name as the primary key to prevent multiple submissions of the same participant.
    name = models.CharField(max_length=100, primary_key=True)
    age  = models.IntegerField()
    num_siblings  = models.IntegerField(default=0)   # Number of siblings.
    env_exposures = models.CharField(max_length=200, blank=True)
    genetic_mutations = models.CharField(max_length=200, blank=True)

    REVIEWS = (
        (0, 'Not Reviewed'),
        (1, 'Reviewed - Accepted'),
        (2, 'Reviewed - Not Accepted'),
    )
    review_status = models.IntegerField(default=0, choices=REVIEWS)  # A dropdown box of 3 choices.

    #  This method is used to provide a more helpful representation of the object.
    def __str__(self):
        return self.name
