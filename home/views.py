from django.shortcuts import render
from .models import Maqola
from django.contrib.auth.decorators import login_required


def maqola(request):
    maqolalar = Maqola.objects.all().order_by('-id')
    context = {
        'maqolalar': maqolalar
    }

    return render(
        request=request,
        template_name='index.html',
        context=context
    )

# @login_required
def w_news(request):
    world_news = Maqola.objects.filter(tag='world').order_by('-id')
    context = {
        'world_news': world_news
    }

    return render(
        request=request,
        template_name='world.html',
        context=context
    )

# @login_required
def local_news(request):
    l_news = Maqola.objects.filter(tag='local').order_by('-id')
    context = {
        'l_news':l_news
    }

    return render(
        request=request,
        template_name='local.html',
        context=context
    )

# @login_required
def sport_news(request):
    s_news = Maqola.objects.filter(tag='sport').order_by('-id')

    context = {
        's_news': s_news
    }

    return render(
        request=request,
        template_name='sport.html',
        context=context
    )

def article_detail(request, id):
    maqola = Maqola.objects.get(id=id)
    ctx = {
        'maqola':maqola
    }
    return render(
        request=request,
        template_name='article_detail.html',
        context=ctx
    )