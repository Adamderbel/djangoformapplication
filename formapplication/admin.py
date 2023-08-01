from django.contrib import admin
from .models import Profile , User
from django.utils.html import format_html
from django.core.mail import send_mail
from django.conf import settings
class Formsadmin(admin.ModelAdmin):
    list_filter=['Situation']
    list_display = ['user','Created_at','status']
    readonly_fields=['user','phone','birth','educational_level','institutions','numberofdiplomas','diplomas','frameworks','languages','databases','libraires','more_about_your_skills','years_of_experience','companies_you_worked_at','why_should_we_hire_you']
    search_fields= ['Situation']
    list_per_page= 10 
    def _(self , obj):
        if obj.Situation == 'Approved':
            return True
        elif obj.Situation== 'Pending':
            return None
        else:
            return False
    _.boolean = True 
    def send_status_email(self, obj):
        if obj.Situation =='Approved':
            subject = 'Congratulations You got approved!'
            message = f'Your application is Approved.We will contact with the details soon'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [obj.user.email]  
        elif obj.Situation=='Rejected':
            subject = 'Sorry You got rejected!'
            message = f'Your application is Rejected.We are sorry to inform you that your application didnt match '
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [obj.user.email]  

        try:
            send_mail(subject, message, from_email, recipient_list)
            return True  # Email sent successfully.
        except Exception as e:
            print(str(e))
            return False
    def status(self , obj):
        if obj.Situation == 'Approved':
            color = '#28a745'
        elif obj.Situation== 'Pending':
            color = '#fea95e'
        else:
            color = '#red'
        self.send_status_email(obj)

        return format_html('<stron><p style="color : {}">{}</p></strong'.format(color , obj.Situation))
    status.allow_tags= True
admin.site.register(Profile,Formsadmin)