from django.utils import timezone

from datetime import datetime

from channel.models import Channel, Message

def get_user_channels(user_id):
	return Channel.objects.filter(users__id=user_id)

def get_channel(channel_id):
	return Channel.objects.get(id=channel_id)

def get_channel_messages(channel_id, limit):
	return (Message.objects
			.filter(channel=channel_id)
			.order_by('-timestamp')
			[:limit:-1]) #get bottom of list

def get_new_channel_messages(channel_id, limit, timestamp):
	timestamp = timezone.make_aware(timestamp, timezone.get_current_timezone())
	messages = get_channel_messages(channel_id, limit)	
	
	for m in messages[::-1]:
		if(m.timestamp > timestamp):
			return messages
	return None
