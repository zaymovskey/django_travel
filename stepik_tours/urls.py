from django.contrib import admin
from django.urls import path
from tours.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main'),
    path('departure/<str:departure>/', departure_view, name='departure'),
    path('tour/<int:id>/', tour_view, name='tour')
]
