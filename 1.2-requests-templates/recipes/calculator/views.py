from django.shortcuts import render
from django.http import HttpResponse

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
    'salat': {
        'огурец, шт': 1,
        'помидор, шт': 1,
        'подсолнечное масло нераф, мл': 20,
        'соль, щепотка': 1
    }
    # можете добавить свои рецепты ;)
}

def index(request):
    return render(request, 'calculator/index.html')


def recipe(request, recipe):
    try:
        if request.GET.get('servings') != None:
            servings = int(request.GET.get('servings'))
        
        content = DATA[recipe]

        if request.GET.get('servings') != None:
            for v, k in content.items():
                content[v] = float('{:.2f}'.format(float(k)*float(servings)))

        context = {
            'recipe' : content,
        }
        
        return render(request, 'calculator/index.html', context)

    except:
        return HttpResponse('<p>Такого рецепта не знаю :(</p>')


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
