import datetime

from django.contrib.auth.models import User
from django.db import models


class Thread(models.Model):
	topic = models.CharField(max_length=100)
	people = models.ManyToManyField(User)

	def get_people_names(self):
		return ",".join([p.username for p in self.people.all()])

class Message(models.Model):
	text = models.TextField()
	thread = models.ForeignKey(Thread)
	timestamp = models.DateTimeField()
	author = models.ForeignKey(User)

