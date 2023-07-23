from django import template

register = template.Library()

@register.filter
def get_status_value(instance, field_name):
    return instance.get_status(field_name)