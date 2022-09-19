from django.urls import path

from Website.views import index

urlpatterns = [
    path('', index, name="Website-index"),
]
