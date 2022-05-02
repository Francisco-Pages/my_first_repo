from django import template

register = template.Library()

@register.filter(name='do_a_cut')
def do_a_cut(value, arg):
    """returns the string reversed"""
    return value.replace(arg, 'Good-Bye')
