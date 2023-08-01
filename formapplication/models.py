from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from multiselectfield import MultiSelectField

SITUATION= (
     ('Pending','Pending'),
     ('Approved','Approved'),
     ('Rejected','Rejected')
)

EDUCATIONAL = (
     ('','Educational Level'),
     ('Sans Bac','Sans Bac'),
     ('Bac +1 ','Bac +1'),
     ('Bac +2','Bac +2'),
     ('Bac +3','Bac +3'),
     ('Bac +4','Bac +4'),
     ('Bac +5','Bac +5'),
     ('Bac +6','Bac +6'),
     ('Bac +7','Bac +7'),
     ('other','other')
)
DIPLOMAS = (
    ('', 'Number Of Diploma/Degree Obtained' ),
    ('1 ','1'),
    ('2 ','2'),
    ('2 ','2'),
    ('3','3'),
    ('more than 3','more than 3')    
)
FRAMEWORKS = (
     ('Laravel','Laravel'),
     ('Angular','Angular'),
     ('Django','Django'),
     ('Flask','Flask'),
     ('Vue','Vue'),
     ('Others','Others'),
  
)
LANGUAGES = (
     ('Python','Python'),
     ('Javascript','Javascript'),
     ('Java','Java'),
     ('C++','C++'),
     ('Ruby','Ruby'),
     ('Others','Others'),
  
)
DATABASES= (
     ('MySql','MySql'),
     ('Postgree','Postgree'),
     ('MongoDB','MongoDB'),
     ('Sqlite3','Sqlite3'),
     ('Oracle','Oracle'),
     ('Others','Others'),
  
)
LIBRAIRES = (
     ('Ajax','Ajax'),
     ('Jquery','Jquery'),
     ('Reactjs','Reactjs'),
     ('scikit-learn','scikit-learn'),
     ('TensorFlow','TensorFlow'), 
     ('Others','Others'),
  
)

EXPERIENCE=(
    ('','Years of experience'),
     ('NO experience','NO experience'),
     ('1 year','1 year'),
     ('2 years','2 years'),
     ('3 years','3 years'),
     ('4 years','4 years'),
     ('5 years','5 years'),
     ('6 years','6 years'),
     ('more','more'),
     
)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth=models.DateField(auto_now=False,auto_now_add=False,verbose_name="Birthday")
    phone=models.CharField(max_length=20, null=True , blank=True)
    Created_at=models.DateTimeField(auto_now_add=True)
    Situation=models.CharField(max_length=50, null=True, choices=SITUATION , default='Pending')
    educational_level=models.CharField(max_length=50, null=True ,choices= EDUCATIONAL, blank=True)
    institutions=models.TextField(max_length=50,null=True, blank=True)
    numberofdiplomas=models.CharField(max_length=50, null=True ,choices= DIPLOMAS ,blank=True)
    diplomas = models.TextField(max_length=50, null=True, blank=True)
    frameworks= MultiSelectField(max_length=50,choices=FRAMEWORKS, default="",blank=True)
    languages= MultiSelectField(max_length=50,choices=LANGUAGES, default="",blank=True)
    databases= MultiSelectField(max_length=50,choices=DATABASES, default="",blank=True)
    libraires= MultiSelectField(max_length=50,choices=LIBRAIRES, default="",blank=True)
    more_about_your_skills=models.TextField(max_length=50, null=True, blank=True)
    years_of_experience=models.CharField(max_length=50, null=True ,choices= EXPERIENCE, blank=True)
    companies_you_worked_at=models.TextField(max_length=50, null=True, blank=True)
    why_should_we_hire_you=models.TextField(max_length=50, null=True, blank=True)
    def __str__(self) :
        return str(self.user)




@receiver(post_save , sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(
            user= instance
        )

