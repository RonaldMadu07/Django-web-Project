from django.shortcuts import render
from django.core.mail import send_mail
from .forms import EnrollForm
from django.conf import settings


# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
    
        #send email
        
        send_mail(
            'Contact Form',
            name,
            email,
            message,
            'settings.EMAIL_HOST_USER', 
            [email],
            fail_silently=False
        )
    
    return render(request, 'index.html')  
     
def form(request):
    if request.method == "POST":
        form = EnrollForm(request.POST or None)
        print(request.POST)

        if form.is_valid():
            form.save()
        else:
            print(form.errors)

        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        gender = request.POST['gender']
        dob = request.POST['dob']
        address = request.POST['address']
        state = request.POST['state']
        telephone = request.POST['telephone']
        email = request.POST['email'] 
        
        enroll_date = request.POST['enroll_date']
            
        return render(request, 'review.html', {
             'firstname': firstname,
                    'lastname': lastname,
                    'gender': gender,
                    'dob': dob,
                    'address': address,
                    'state': state,
                    'telephone': telephone,
                    'email': email,
                    
                    'enroll_date': enroll_date,  
        })
            
    else:
        return render(request, 'form.html', {})
    

def appreciation(request):
   
    return render(request, 'appreciation.html')

def review(request):
    
    return render(request, 'review.html', {}) 