from django.template import Library

from page.models import Profile

register = Library()

@register.inclusion_tag('page/partials/network_links.html')
def network_links(profile_id: int):
    """
    Render the social network links for a given profile.
    """
    try:
        profile = Profile.objects.get(id=profile_id)
        social_links = profile.social_links.all()
    except Profile.DoesNotExist:
        return {
            'networks': [],
            'profile': None,
        }
    return {
        'profile': profile,
        'networks': social_links,
    }