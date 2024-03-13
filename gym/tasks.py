from core.celery import app
from django.shortcuts import render
from users.models import User
from datetime import datetime
from django.utils import timezone
import pytz

@app.task
def beat_func():
    users = User.objects.filter(subscription_is_activate=False)
    usernames = [user.username for user in users]
    return usernames


def convert_date(data):
    data = datetime.strptime(data, "%Y-%m-%d")
    data = timezone.make_aware(data, timezone=pytz.UTC)
    return data


def page(request):
    if request.method == 'POST':
        beat_func.delay()
        min_age = request.POST.get('min_age')
        max_age = request.POST.get('max_age')
        min_birtday = convert_date(request.POST.get('min_birtday'))
        max_birtday = convert_date(request.POST.get('max_birtday'))
        min_visit = convert_date(request.POST.get('min_visit'))
        max_visit = convert_date(request.POST.get('max_visit'))
        min_join = convert_date(request.POST.get('min_join'))
        max_join = convert_date(request.POST.get('max_join'))
        active = request.POST.get('active')
        users = User.objects.filter(age__gte=min_age, age__lte=max_age, subscription_is_activate=active,
                                    birth_day__gte=min_birtday, birth_day__lte=max_birtday,
                                    last_login__gte=min_visit, last_login__lte=max_visit,
                                    date_joined__gte=min_join, date_joined__lte=max_join)
        return render(request, 'gym/includes/templateV2.html', {'users': users})
    else:
        return render(request, 'gym/includes/templateV2.html')

# @app.task
# def process_post_request(min_age, max_age, min_birtday, max_birtday,
#                                           min_visit, max_visit, min_join, max_join, active):
#
#     users = User.objects.filter(age__gte=min_age, age__lte=max_age, subscription_is_activate=active,
#                                 birth_day__gte=min_birtday, birth_day__lte=max_birtday,
#                                 last_login__gte=min_visit, last_login__lte=max_visit,
#                                 date_joined__gte=min_join, date_joined__lte=max_join)
#     return users.get()
#
#
# def page(request):
#     if request.method == 'POST':
#         min_age = request.POST.get('min_age')
#         max_age = request.POST.get('max_age')
#         min_birtday = convert_date(request.POST.get('min_birtday'))
#         max_birtday = convert_date(request.POST.get('max_birtday'))
#         min_visit = convert_date(request.POST.get('min_visit'))
#         max_visit = convert_date(request.POST.get('max_visit'))
#         min_join = convert_date(request.POST.get('min_join'))
#         max_join = convert_date(request.POST.get('max_join'))
#         active = request.POST.get('active')
#         user = process_post_request.delay(min_age, max_age, min_birtday, max_birtday, min_visit, max_visit, min_join, max_join, active)
#
#         return render(request, 'gym/includes/templateV2.html',{'users': user})
#     else:
#         return render(request, 'gym/includes/templateV2.html')

