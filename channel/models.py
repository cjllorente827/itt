from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

import json

class Channel(models.Model):
	name = models.CharField(max_length=100)
	users = models.ManyToManyField(User)

	def get_users_names(self):
		return ",".join([p.username for p in self.users.all()])

class Message(models.Model):
	text = models.TextField()
	channel = models.ForeignKey(Channel)
	timestamp = models.DateTimeField()
	op = models.ForeignKey(User)

	@classmethod
	def create_from_request(cls, request):
		body = json.loads(request.body.decode(encoding='UTF-8'))
		new_msg = cls(
			text=body["messageBody"], 
			channel=Channel(id=body["channelId"]), 
			op=User(id=request.user.id), 
			timestamp=timezone.now())
		new_msg.full_clean()
		return new_msg


