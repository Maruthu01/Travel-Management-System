# Create your views here.
from django.shortcuts import render,redirect
from .models import Register
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import login,authenticate
from django.conf import settings
from .forms import WhatsAppForm
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm,ReviewForm
from .models import Review,CustomerReview



def Welcome(request):
    reviews = Review.objects.all()  
    return render(request, 'prac.html', {'reviews': reviews})   


@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('Welcome')  
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})

@login_required
def update_review(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            return redirect('Welcome')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'update_review.html', {'form': form})

@login_required
def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)
    if request.method == 'POST':
        review.delete()
        return redirect('Welcome')
    return render(request, 'delete_review.html', {'review': review})




@login_required
def list_reviews(request):
    reviews = CustomerReview.objects.filter(user=request.user)
    return render(request, 'reviews/list_reviews.html', {'reviews': reviews})



def Login_page(request):
    if request.method == 'POST':
        F_name = request.POST['F_name']
        Password = request.POST['Password']

        user = authenticate(request, username=F_name, password=Password)
        if user is not None:
            login(request, user) 
            return redirect('Welcome')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
        
            return redirect('login')  
    return render(request, 'login.html')



def Register1(request):
    if request.method == 'POST':
        F_name = request.POST['F_name']
        L_name = request.POST['L_name']
        Email_id = request.POST['Email_id']
        Mob_num = request.POST['Mob_num']
        Password = request.POST['Password']
        Conf_Pass = request.POST['Conf_password']
        terms_checked = request.POST.get('terms_checked')

        if not Email_id.endswith('@gmail.com'):
            messages.warning(request, 'Please enter a valid Gmail address.')
            return redirect('Register')
        
        if len(Mob_num) != 10:
            messages.warning(request,'Please enter an valid Mobile number')
            return redirect('Register')
            
        
        if User.objects.filter(email=Email_id).exists():
            messages.warning(request, f'The email "{Email_id}" is already registered.')
            return redirect('Register')

        if Password == Conf_Pass:
            if terms_checked:
                
                user = User.objects.create_user(
                    username=F_name,
                    email=Email_id,
                    password=Password,
                    first_name=F_name,
                    last_name=L_name
                )
                user.save()
                messages.success(request, 'You are successfully registered. Please login.')
                return redirect('login')
            else:
                messages.warning(request, 'You must agree to the terms and conditions.')
                return redirect('Register')
        else:
            messages.warning(request, 'Password mismatched. Please try again.')
            return redirect('Register')
    else:
        return render(request, 'pro.html')
    
    

def Login1(request):
    return render(request,'Login1.html')

def Payment(request):
    return render(request,'eg.html')

def About(request):
    return render(request,'Aboutus.html')        


def send_whatsapp_message(request):
    if request.method == 'POST':
        form = WhatsAppForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']

            
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

            try:
                
                client.messages.create(
                    body=message,
                    from_=f'whatsapp:{settings.TWILIO_PHONE_NUMBER}',  
                    to=f'whatsapp:{phone_number}'  
                )
            except TwilioRestException as e:
                print(f"Twilio exception occurred: {e}")
                return render(request, 'Message.html', {'form': form, 'error': str(e)})

            return redirect('success')

    else:
        form = WhatsAppForm()

    return render(request, 'Message.html', {'form': form})

def Success(request):
    return render (request,'success.html')

def Bookin(request):
    return render (request,'Booking_area.html')









        