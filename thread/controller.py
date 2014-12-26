from django.utils import timezone

from datetime import datetime

from thread.models import Thread, Message

def get_user_threads(user_id):
	return Thread.objects.filter(people__pk=user_id)

def get_thread(thread_id):
	return Thread.objects.get(pk=thread_id)

def get_thread_messages(thread_id, limit):
	return (Message.objects
			.filter(thread=thread_id)
			.order_by('-timestamp')
			[:limit:-1]) #get bottom of list

def get_new_thread_messages(thread_id, limit, timestamp):
	timestamp = timezone.make_aware(timestamp, timezone.get_current_timezone())
	messages = get_thread_messages(thread_id, limit)	
	
	for m in messages[::-1]:
		if(m.timestamp > timestamp):
			return messages
	return None
