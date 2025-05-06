from django import template


register = template.Library()


@register.filter
def rating_stars(rating):
    stars = ''
    for i in range(rating):
        stars += "★"
    for i in range(5 - rating):
        stars += "☆"
    return stars


@register.simple_tag(takes_context=True)
def display_owner(context, user):
    if user == context['user']:
        return "vous avez"
    return f"{user.username} a"
