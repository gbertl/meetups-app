from django.shortcuts import render

from .models import Meetup

def index(request):
    meetups = Meetup.objects.all()

    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })

def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)

        return render(request, 'meetups/meetup-detail.html', {
            'meetup_title': selected_meetup.title,
            'meetup_description': selected_meetup.description,
            'meetup_found': True
        })
    except Exception as e:
        return render(request, 'meetups/meetup-detail.html', {
            'meetup_found': False
        })
