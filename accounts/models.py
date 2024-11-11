from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    
    
def on_send_mail(sender, **kwargs):
    if kwargs['created'] :
        user = kwargs['instance']
        send_mail('가입인사','가입을 환영합니다.', 'admin@sky.com', [user.email], fail_silently=False)
post_save.connect(on_send_mail, sender=settings.AUTH_USER_MODEL)
