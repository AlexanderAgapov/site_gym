from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=100, unique=True, blank=False, verbose_name='Телефон', default='')
    subscription_is_activate = models.BooleanField(default=True, verbose_name='Активирован')
    birth_day = models.DateTimeField(auto_now=True, verbose_name='День рождения')
    age = models.PositiveIntegerField(default=0, verbose_name='Возраст')

    def __str__(self):
        return f'{self.username}, {self.age}'


# user_list = []
# from faker import Faker
# from users.models import User
# from datetime import datetime, timedelta
# import random
# import pytz
#
# fake = Faker()
# for _ in range(1000):
#     ffirst_name = fake.first_name()
#     flast_name = fake.last_name()
#     frandom_date = fake.date_of_birth()
#     flrandom_date = datetime.utcnow() - timedelta(days=random.randint(1, 90))
#     faware_random_date = pytz.utc.localize(flrandom_date)
#     fusername = fake.user_name()
#     femail = fake.email()
#     fpassword = fake.password()
#     fphone_number = str(fake.unique.phone_number())
#     while fphone_number in user_list:
#         fphone_number = str(fake.unique.phone_number())
#     user_list.append(fphone_number)
#     fsubscription_is_active = fake.boolean()
#     fage = fake.random_int(18, 80)
#     user = User.objects.create_user(username=fusername, email=femail, password=fpassword, phone_number=fphone_number, age=fage, first_name=ffirst_name, last_name=flast_name, last_login=faware_random_date, birth_day=frandom_date)
#     user.save()
