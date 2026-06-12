from django.urls import path
from . import views

urlpatterns=[

path('',views.home,name="home"),

path('recipe/<int:id>/',views.recipe_detail,name="recipe_detail"),

path('categories/',views.categories,name="categories"),

path('cuisine/<str:cuisine>/',views.cuisine_items,name="cuisine"),

path('search/',views.search,name="search"),

path('about/',views.about,name="about"),

path('contact/',views.contact,name="contact"),

]