from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from cities.forms import HtmlForm, CityForm
from cities.models import City

__all__ = (
    'home', 'CityDetailView'
)


def home(request, pk=None):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    # if pk:
    # city = get_object_or_404(City, id=pk)
    # city = City.object.filter(id=pk).first()
    # city = City.object.get(id=pk)
    # context = {'object': city}
    # return render(request, 'cities/detail.html', context)

    form = CityForm()
    gs = City.objects.all()
    context = {'objects_list': gs, 'form': form}
    return render(request, 'cities/home.html', context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'
