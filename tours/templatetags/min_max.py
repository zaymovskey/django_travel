from django import template

register = template.Library()


@register.filter(name='min_max')
def min_max(l, string):
    if string == 'max':
        return max(l)
    elif string == 'min':
        return min(l)
    else:
        return ''
