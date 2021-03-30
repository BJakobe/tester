from django.urls import path

from .views import HomePageView, index_card_view

urlpatterns = [
	path('', HomePageView.as_view(), name="index"),
	path('index_card', index_card_view, name="index_card")
]

#intro_index


#HUUUHH y index no longer exist ambotzzzz before #30 mar ano raw????