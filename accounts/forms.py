from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django import forms

class SignupForm(UserCreationForm):
    phone_number = forms.CharField()
    address = forms.CharField()
    
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', )
        
    def save(self):
        user = super().save()
        Profile.objects.create(user=user,
                               phone_number = self.cleaned_data['phone_number'],
                               address = self.cleaned_data['address'])
        return user