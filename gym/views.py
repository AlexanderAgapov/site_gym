from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView
from django.http import HttpResponse
from rest_framework import generics, viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from .serializers import GymSerializer
from users.models import User
from .forms import AddEventForm
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from django.core.cache import cache
from django.utils.decorators import method_decorator

def home_clients(request):
    return HttpResponse('Страница для клиентов')


def home_admin(request):
    return HttpResponse('Страница для персонала')

#@cache_page(60, key_prefix='site1')
class GymViewSet(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.ListModelMixin,
                 GenericViewSet):
    queryset = User.objects.filter(is_superuser=True).values('username', 'email')
    serializer_class = GymSerializer
    #permission_classes = (IsAuthenticated, )

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super(GymViewSet, self).dispatch(*args, **kwargs)

class AddEvent(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    form_class = AddEventForm
    template_name = 'gym/includes/add_event.html'
    success_url = reverse_lazy('add_event')
    title_page = 'Добавление мероприятия'
    permission_required = 'gym.add_event'


class GymHome(ListView):
    template_name = 'gym/index.html'
    context_object_name = 'posts'
    title_page = 'Главная страница'


# def my_functions():
#     return([i for i in range(1000)])
#
#
# def page(request):
#     if request.method == 'POST':
#         result = my_functions()
#         return render(request, 'gym/includes/my_template.html', {'result': result})
#     else:
#         return render(request, 'gym/includes/my_template.html')

