from django.shortcuts import render
from .api import get_all_recipes,get_recipe,search_recipes,get_by_cuisine


def home(request):

    recipes = get_all_recipes()[:6]

    return render(request,"home.html",{"recipes":recipes})


def recipe_detail(request,id):

    recipe = get_recipe(id)

    return render(request,"recipe_detail.html",{"recipe":recipe})


def categories(request):

    recipes = get_all_recipes()

    cuisines = list(set([r['cuisine'] for r in recipes]))

    return render(request,"categories.html",{"cuisines":cuisines})


def cuisine_items(request,cuisine):

    items = get_by_cuisine(cuisine)

    return render(request,"recipe_list.html",{"recipes":items,"title":cuisine})


def search(request):

    q = request.GET.get("q")

    recipes = search_recipes(q)

    return render(request,"recipe_list.html",{"recipes":recipes,"title":"Search"})


def about(request):

    return render(request,"about.html")


def contact(request):

    return render(request,"contact.html")