from . import models
from django.views import generic
from sport_inv.models import Slogan, TopProduct, YouTubeVideo
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse


class HomePageView(generic.ListView):
    template_name = 'home/main.html'
    context_object_name = 'main_menu_list'
    model = Slogan
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slogan'] = models.Slogan.objects.order_by('-id')
        context['top_products'] = models.TopProduct.objects.order_by('-id')[:5]
        context['youtube_url'] = models.YouTubeVideo.objects.order_by('-id')[:5]
        return context


def about_us_view(request):
    if request.method == "GET":
        return HttpResponse("")


def contact_us_view(request):
    if request.method == "GET":
        return HttpResponse("")
