from django import template

register = template.Library()

@register.filter
def format_datetime(datetime, formatStr):
	return formatStr.format(d=datetime)