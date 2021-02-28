from django.shortcuts import render, get_object_or_404

from cities.models import City

__all__ = (
    'home',
)


def home(request, pk=None):
    if pk:
        city = get_object_or_404(City, id=pk)
        # city = City.object.filter(id=pk).first()
        # city = City.object.get(id=pk)

        context = {'object': city}
        return render(request, 'cities/detail.html', context)
    gs = City.objects.all()
    context = {'objects_list': gs}
    return render(request, 'cities/home.html', context)