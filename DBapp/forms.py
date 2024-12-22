from django import forms
# from .models import Article
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text', 'review_image']


class WhatsAppForm(forms.Form):
    phone_number = forms.CharField(label='Phone Number', max_length=20)
    message = forms.CharField(label='Message', widget=forms.Textarea,initial='Hello! Your ticket has booked, You will get an tkt status before boarding')




class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

