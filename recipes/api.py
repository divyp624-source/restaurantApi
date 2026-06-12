import requests

BASE_URL = "https://dummyjson.com/recipes"


def get_all_recipes():
    res = requests.get(BASE_URL)
    return res.json()['recipes']


def get_recipe(id):
    res = requests.get(f"{BASE_URL}/{id}")
    return res.json()


def search_recipes(query):
    res = requests.get(f"{BASE_URL}/search?q={query}")
    return res.json()['recipes']


def get_by_cuisine(cuisine):
    res = requests.get(BASE_URL)
    recipes = res.json()['recipes']
    return [r for r in recipes if r['cuisine'].lower() == cuisine.lower()]