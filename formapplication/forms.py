from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django.contrib.auth.models import User 
from .models import Profile
class Lowercase(forms.CharField):
    def to_python(self,value):
        return value.lower()
class SingupForm(UserCreationForm):
    email= Lowercase(
        min_length=3,max_length=50, 
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',
        message="Put a valid email address!")],
        required=True,
        widget=forms.TextInput(attrs={'placeholder':'Email'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
class UserForm(forms.ModelForm):
    first_name= forms.CharField(
        label='First name',min_length=3,max_length=50, 
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
        message="only letters are allowed!")],
        widget=forms.TextInput(attrs={'placeholder':'First name'}))
    last_name= forms.CharField(
        label='Last name',min_length=3,max_length=50, 
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
        message="only letters are allowed!")],
        widget=forms.TextInput(attrs={'placeholder':'Last name'}))
    email= Lowercase(
        label='Email address',min_length=3,max_length=50, 
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',
        message="Put a valid email address!")],
        widget=forms.TextInput(attrs={'placeholder':'Email'}))
    class Meta:
        model=User
        fields=['username', 'email' ,'first_name' ,'last_name']
class ProfileForm(forms.ModelForm):
     diplomas= forms.CharField(
        label='What are your diplomas',min_length=3,max_length=100, 
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
        message="only letters are allowed!")],
        required=False,
        widget=forms.Textarea(attrs={'placeholder':'Diplomas','rows':4}))
     institutions= forms.CharField(
        label='Which institutions did you go for',min_length=20,max_length=400, 
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
        message="only letters are allowed!")],
        required=False,
        widget=forms.Textarea(attrs={'placeholder':' Institutions','rows':4}))
     more_about_your_skills= forms.CharField(
        label='Tell us more about your skills', 
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
        message="only letters are allowed!")],
        required=False,
        widget=forms.Textarea(attrs={'placeholder':'Tell us about your skills','rows':10}))
     companies_you_worked_at= forms.CharField(
        label='which companies did you work for ', 
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
        message="only letters are allowed!")],
        required=False,
        widget=forms.Textarea(attrs={'placeholder':'Tell us about your skills','rows':4}))
     why_should_we_hire_you= forms.CharField(
        label='Tell us why we should hire you', 
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
        message="only letters are allowed!")],
        required=False,
        widget=forms.Textarea(attrs={'placeholder':'Tell us about your skills','rows':10}))
     phone=forms.CharField(
         validators=[RegexValidator(r'^[0-9]*$',
              message="only numbers are allowed!")],
       widget=forms.TextInput( attrs={
             'placeholder':'Enter your phone number',
       }))
     birth=forms.DateField(
       widget=forms.DateInput( 
        attrs={ 'style':'cursor:pointer',
               'type':'date',}))
     class Meta:
        model = Profile
        fields =['phone','birth','educational_level','institutions','numberofdiplomas','diplomas','frameworks','languages','databases','libraires','more_about_your_skills','years_of_experience','companies_you_worked_at','why_should_we_hire_you']
