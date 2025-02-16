from django import forms
from .models import *

class campform(forms.ModelForm):

    class Meta:
        model = camp
        fields = ['camp_id','camp_name','address','district','city','panchayat','contact']

class loginform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control rounded-left'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control rounded-left'}))
    class Meta:
        model = login
        fields = ['email','password']
        
class Login2Form(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control rounded-left'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control rounded-left'}))



class publicform(forms.ModelForm):

    class Meta:
        model = public
        fields = ['name','address','district','city','state','contact']

class volunteerform(forms.ModelForm):

    class Meta:
        model = volunteer
        fields = ['name','gender','age','contact']

class stationform(forms.ModelForm):

    class Meta:
        model = station
        fields = ['station_id','address_line1','address_line2','district','city','contact','authentication']

class camp_prof(forms.Form):

    class Meta:
        model = camp
        fields = ['camp_id','camp_name','address','district','city','panchayat','contact']

class login_email_form(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control rounded-left'}))
    class Meta:
        model = login
        fields = ['email']

class public_prof(forms.Form):
    class Meta:
        model = public
        fields = ['name','address','district','city','state','contact']

class station_prof(forms.Form):
    class Meta:
        model = station
        fields = ['station_id','address_line1','address_line2','district','city','contact','authentication']


class volunteer_prof(forms.Form):
    class Meta:
        model = volunteer
        fields = ['name','gender','age','contact']




  