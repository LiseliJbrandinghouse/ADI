from django.urls import path
from .views import documents, documents, home, speakers,registration,donate,vote,accommodation
from mysite import views

urlpatterns = [
    path('', home, name='home'),
    path('speakers/', speakers, name='speakers'),
    path('registration/', registration, name='registration'),
    path('donate/', donate, name='donate'),
    path('vote/', vote, name='vote'),
    path('accommodation/', accommodation, name='accommodation'),
   path('documents/', views.documents, name='documents'),
    path('media/', views.media, name='media'),
    path('fife/', views.fife, name='fife'),
    path('outcome/', views.outcome, name='outcome'),
]