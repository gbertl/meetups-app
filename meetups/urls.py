from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('meetups/', views.index, name='all-meetups'),
    path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetup-detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
