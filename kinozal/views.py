from django.views.generic import TemplateView, ListView, DetailView

from . models import Film
from . import selectors


class IndexViews(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context |= {
            'today_recomendation': selectors.random_films_selector(),
            'max_rating': selectors.max_rating_selector(),
            'max_rating2': selectors.max_rating_selector(6, 12),
        }
        return context


class SingleMoviesViews(DetailView):
    template_name = 'single-movies.html'
    model = Film
    context_object_name = 'film'
    slug_url_kwarg = 'slug'
    queryset = Film.objects.prefetch_related('categories')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context |= {
            'related_films': selectors.related_film_selector(self.object),
            'related_director': selectors.related_director_selector(self.object),
        }
        return context


class MoviesCategoryViews(ListView):
    template_name = 'movies.html'
    model = Film
    context_object_name = 'films_category'
    slug_url_kwarg = 'slug'
    paginate_by = 30

    def get(self, request, *args, **kwargs):
        self.release_year = Film.objects.get(name=self.request.GET['release_year'])\
            if self.request.GET.get('release_year') else None
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        _filter = {'categories__slug': self.kwargs.get('slug')}

        if self.release_year:
            _filter['release_year__name'] = self.release_year.name

        return Film.objects.prefetch_related('categories').filter(**_filter)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context |= {
            'years': selectors.years_selector(),
            'categories': selectors.categories_selector(),
            'top_film': selectors.max_rating_selector(10, 15),
        }
        return context


class MoviesOlView(ListView):
    template_name = 'movies.html'
    model = Film
    paginate_by = 30
    queryset = Film.objects.all()
    context_object_name = 'films_category'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context |= {
            'years': selectors.years_selector(),
            'categories': selectors.categories_selector(),
            'top_film': selectors.max_rating_selector(10, 15),
        }
        return context
