from django.shortcuts import render
from .models import Advertisement


def home(request):
    advertisement = Advertisement.objects.last()

    is_video = advertisement.banner.url.endswith('.mp4') if advertisement.banner else False
    
    return render(request, 'main/home.html', {
        'advertisement': advertisement,
        'is_video': is_video
    })

    return render(request, 'main/home.html')


def base(request):
    return render(request, 'main/base.html')


def shop_all(request):
    return render(request, 'main/shop_all.html')


def ingredients(request):
    return render(request, 'main/ingredients.html')


# footer components:
def shipping_policy(request):
    return render(request, 'main/components/footer/shipping_policy.html')


def terms_and_conditions(request):
    return render(request, 'main/components/footer/terms_and_conditions.html')


def website_terms_and_conditions(request):
    return render(request, 'main/components/footer/website_terms_and_conditions.html')


def privacy_policy(request):
    return render(request, 'main/components/footer/privacy_policy.html')


def acceptable_use_policy(request):
    return render(request, 'main/components/footer/acceptable_use_policy.html')
