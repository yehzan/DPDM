from django.urls import path
from . import views
urlpatterns=[
    path('index',views.index,name='index'),
    path('admin',views.sidebar,name='admin'),
    path('login',views.login_index,name='login'),
    path('campregi',views.campreg,name='campregi'),
    path('publicpath',views.publicreg,name='publicpath'),
    path('volpath',views.volunteerreg,name='volpath'),
    path('stationpath',views.stationreg,name='stationpath'),
    path('camppage',views.camp_entry,name='camppage'),
    path('publicpage',views.public_entry,name='publicpage'),
    path('volunteerpage',views.volunteer_entry,name='volunteerpage'),
    path('stationpage',views.station_entry,name='stationpage'),
    path('camp_profile_path',views.camp_pro,name='camp_profile_path'),
    path('public_profile_path',views.public_pro,name='public_profile_path'),
    path('station_profile_path',views.station_pro,name='station_profile_path'),
    path('volunteer_profile_path',views.volunteer_pro,name='volunteer_profile_path')
]
