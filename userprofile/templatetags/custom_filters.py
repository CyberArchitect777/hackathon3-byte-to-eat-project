from django import template
register = template.Library()

# Converts ratings /5 in to stars


@register.filter
def star_rating(value):
    try:
        value = float(value)
    except (ValueError, TypeError):
        return ''
    full_stars = int(value)
    half_star = 1 if value - full_stars >= 0.5 else 0
    empty_stars = 5 - full_stars - half_star
    stars = ('<i class="fa-solid fa-star"></i>' * full_stars) + \
            ('<i class="fa-solid fa-star-half"></i>' * half_star) + \
            ('<i class="fa-regular fa-star"></i>' * empty_stars)
    return stars


star_rating.is_safe = True
