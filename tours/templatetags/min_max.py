from django import template

register = template.Library()


@register.filter(name='min_max')
def min_max(list, string):
    if string == 'max':
        return max(list)
    elif string == 'min':
        return min(list)
    else:
        return ''
