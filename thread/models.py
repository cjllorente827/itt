from django.contrib.auth.models import User
from django.db import models

from datetime import datetime
import json

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

	@classmethod
	def create_from_request(cls, request):
		body = json.loads(request.body.decode(encoding='UTF-8'))
		new_msg = cls(
			text=body["messageBody"], 
			thread=Thread(id=body["threadId"]), 
			author=User(id=request.user.id), 
			timestamp=datetime.now()
		)
		new_msg.full_clean()
		return new_msg


