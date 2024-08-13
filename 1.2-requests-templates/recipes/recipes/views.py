from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'sandwich': {
        'хлеб, ломтик': 2,
        'курица, ломтик': 2,
        'огурец, ломтик': 3,
        'сыр, ломтик': 1,
        'соус Цезарь, г': 15
    },
    'salad': {
        'огурец, г': 50,
        'помидор, г': 45,
        'перец, г': 35,
        'чеснок, г': 1,
        'соевый соус, г': 10
    }

}

def recipe_view(request, dish_name):
    recipe = DATA.get(dish_name)
    servings = int(request.GET.get('servings', 1))

    if recipe:
        portioned_recipe = {ingredient: amount * servings for ingredient, amount in recipe.items()}
        context = {
            'recipe': portioned_recipe,
            'recipe_name': dish_name
        }
    else:
        context = {
            'recipe': None
        }
    return render(request, 'calculator/index.html', context)