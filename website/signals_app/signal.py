from django.contrib.auth.signals import user_logged_in #signal
from django.contrib.auth.signals import user_logged_out #signal
from django.db.models.signals import pre_save #signal

from django.contrib.auth.models import User #sender

from django.dispatch import receiver  #receiver

def login_success(sender, request, user, **kwargs):
    print(f'user {user.username} logged in')
    print(f'IP address {request.get_host()}')
    print(f'sender {sender}')
    print(f'kwargs {kwargs}')    
user_logged_in.connect(login_success, sender=User)

def logout_success(sender, request, user, **kwargs):
    print(f'user {user.username} logged out')
    print(f'IP address {request.get_host()}')
    print(f'sender {sender}')
    print(f'kwargs {kwargs}')
user_logged_out.connect(logout_success, sender=User)

@receiver(pre_save, sender=User)
def user_pre_save(sender, instance, **kwargs):
    print(f'sender {sender}')
    print(f'user {instance} logged in')