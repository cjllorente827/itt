
import datetime

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
