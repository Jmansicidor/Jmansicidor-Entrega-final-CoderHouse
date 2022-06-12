import mailbox

from django.db import models

user_sex = [
    (1, 'Male'),
    (2, 'Female'),
    (3, 'Other')
]


class User(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user_sex = models.IntegerField(
        null=False, blank=False,
        choices=user_sex
    )
    mailbox = models.CharField()

    def __str__(self):
        return f'User {self.id}: {self.name} {self.last_name} {self.mailbox}'
