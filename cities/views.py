from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from cities.forms import HtmlForm, CityForm
from cities.models import City

__all__ = (
    'home', 'CityDetailView',
    'CityCreateView', 'CityUpdateView',
    'CityDeleteView'
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


class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')


class CityUpdateView(UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')


class CityDeleteView(DeleteView):
    model = City
    # template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:home')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
