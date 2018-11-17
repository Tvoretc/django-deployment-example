from django import template

register = template.Library()
@register.filter(name='cut')
def cut(value, arg):
    return value.replace(arg,'222')

#register.filter('cut2', cut2)
