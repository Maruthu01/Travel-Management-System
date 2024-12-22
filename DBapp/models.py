from django.db import models
from django import forms
from django.contrib.auth.models import User




class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    review_text = models.TextField()
    review_image = models.ImageField(upload_to='reviews/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"{self.user.username} - {self.review_text[:50]}"
    
    
class CustomerReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    review_text = models.TextField()
    review_image = models.ImageField(upload_to='reviews/')  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review by {self.user.username}"
    



class Register(models.Model):
    F_name = models.CharField(max_length=100)
    L_name = models.CharField(max_length=100)
    Email_id = models.EmailField()
    Mob_num = models.CharField(max_length=15)
    Password = models.CharField(max_length=100)


    
    
    def __str__(self) -> str:
        return self.F_name
    
    

    class WhatsAppForm(forms.Form):
        phone_number = forms.CharField(label='Phone Number', max_length=20)
        message = forms.CharField(label='Message', widget=forms.Textarea)

    def __str__(self )-> str:
        return self.message
    




































    class Destination(models.Model):
        name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    