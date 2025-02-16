from django.db import models

# Create your models here.
class login(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    usertype = models.CharField(max_length=50)

class camp(models.Model):
    camp_id = models.CharField(max_length=50)
    camp_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    panchayat = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    login_id = models.ForeignKey('login',on_delete=models.CASCADE)


class public(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    login_id = models.ForeignKey('login',on_delete=models.CASCADE)

class volunteer(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    age = models.IntegerField()
    contact = models.CharField(max_length=10)
    login_id = models.ForeignKey('login',on_delete=models.CASCADE)

class station(models.Model):
    station_id = models.CharField(max_length=50)
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    authentication = models.IntegerField()
    login_id = models.ForeignKey('login',on_delete=models.CASCADE)