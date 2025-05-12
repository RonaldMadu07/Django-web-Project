from django.db import models
from django.utils import timezone


# Create your models here.

class Enroll(models.Model): 
    
    GENDER_CHOICES = [
        ('M', 'MALE'),
        ('F', 'FEMALE')
    ]

    STATE_CHOICES = [
        ('Abia', 'Abia State'),
        ('Adamawa', 'Adamawa State'),
        ('Akwa-Ibom', 'Akwa-Ibom State'),
        ('Anambara', 'Anambara State'),
        ('Bauchi', 'Bauchi State'),
        ('Bayelsa', 'Bayelsa State'),
        ('Benue', 'Benue State'),
        ('Bornu', 'Bornu State'),
        ('Cross-River', 'Cross-River State'),
        ('Delta', 'Delta State'),
        ('Ebonyi', 'Ebonyi State'),
        ('Edo', 'Edo State'),
        ('Ekiti', 'Ekiti State'),
        ('Enugu', 'Enugu State'),
        ('Gombe', 'Gombe State'),
        ('Imo', 'Imo State'),
        ('Jigawa', 'Jigawa State'),
        ('Kaduna', 'Kaduna State'),
        ('Kano', 'Kano State'),
        ('Kastina', 'Kastina State'),
        ('Kebbi', 'Kebbi State'),
        ('Kogi', 'Kogi State'),
        ('Kwara', 'Kwara State'),
        ('Lagos', 'Lagos State'),
        ('Nassawara', 'Nassawara State'),
        ('Niger', 'Niger State'),
        ('Ogun', 'Ogun State'),
        ('Ondo', 'Ondo State'),
        ('Oyo', 'Oyo State'),
        ('Plateau', 'Plateau State'),
        ('Rivers', 'Rivers State'),
        ('Sokoto', 'Sokoto State'),
        ('Taraba', 'Taraba State'),
        ('Yobe', 'Yobe State'),
        ('Zamfara', 'Zamfara State'),
        ('FCT', 'F.C.T Abuja'),
    ]

    firstname = models.CharField('First Name',max_length=20)

    lastname = models.CharField('Last Name', max_length=20)
   
    gender = models.CharField('Gender', max_length=1, choices=GENDER_CHOICES)

    dob = models.DateField('Date of Birth', default='2020-05-05')

    address = models.CharField('Address', max_length=30, default='')

    state = models.CharField('State Of Origin', max_length=36, choices=STATE_CHOICES, default='Select your state')
    
    telephone = models.CharField('Telephone', max_length=11) 
            
    email = models.EmailField('Email', max_length=50, default='ronald@gmail.com')

    passport = models.ImageField('Passport', upload_to='images/', null=True, blank=True)
    
    enroll_date = models.DateField('Enrollment Date', default=timezone.now)
    

    def __str__(self): 
        return self.firstname + ' ' + self.lastname 