from django.shortcuts import render
from page.models import Profile

def home(request, slug=None):
    """
    Render the home page.
    """
    profile = Profile.objects.get(user__username='arison62')
    if not slug:
        # Handle the case where a slug is provided
        # You can add logic here to fetch and display specific content based on the slug
        pass
    else:
        try:
            profile = Profile.objects.get(slug=slug)
        except Profile.DoesNotExist:
            pass
    return render(request, 'page/home.html', {
        'profile': profile,
    })
