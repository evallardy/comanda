from django import template

register = template.Library()

@register.filter
def has_perm_with_args(user, perm):
    return user.has_perm(perm)