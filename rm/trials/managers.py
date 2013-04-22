"""
Custom managers for Trials.
"""
import datetime

from django.db import models

td = lambda: datetime.date.today()

class ActiveManager(models.Manager):
    """
    Custom manager for single user trials.

    Mostly API sugar
    """

    def active(self):
        """
        Return a queryset representing currently active trials.

        Return: Queryset
        Exceptions: None
        """
        return self.filter(start_date__lte=td(), finish_date__gte=td())

    def starting_today(self):
        """
        Return a queryset representing trials that start today.

        Return: Queryset
        Exceptions: None
        """
        return self.filter(start_date=td())



class SingleUserTrialManager(ActiveManager):
    pass

class RmTrialManager(ActiveManager):
    pass