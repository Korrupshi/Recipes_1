from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Recipe
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
# Homepage view
def home(request):
    total_recipes = Recipe.objects.all().count()
    recipes = Recipe.objects.all()
    context = {
        "title": "Homepage",
        "total_recipes": total_recipes,
        "recipes": recipes,
    }

    return render(request, "home.html", context)

# Search function
def search(request):
    recipes = Recipe.objects.all()

    if "search" in request.GET:
        query = request.GET.get("search")
        queryset = recipes.filter(Q(title__icontains=query))
        results = queryset.filter(Q(title__icontains=query))
        topic = ["dinner", "lunch", "side"]

    if request.GET.get("side"):
        results = queryset.filter(Q(topic__title__icontains="side"))
        topic = "side"
    elif request.GET.get("lunch"):
        results = queryset.filter(Q(topic__title__icontains="lunch"))
        topic = "lunch"
    elif request.GET.get("dinner"):
        results = queryset.filter(Q(topic__title__icontains="dinner"))
        topic = "dinner"

    total = results.count()

    #Multiple pages for the search results
    paginator = Paginator(results, 10)
    page = request.GET.get("page")
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)

    context = {
        "topic": topic,
        "page": page,
        "total": total,
        "query": query,
        "results": results,
        "recipes": recipes,
    }
    return render(request, "filter.html", context)

# Detail page
def detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    context = {
        "recipe": recipe,
    }
    return render(request, "detail0.html", context)



