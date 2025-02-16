
from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from .models import *
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request,'usercontent.html')

def admin_index(request):
    return render(request,'admin/maincontent.html')


def sidebar(request):
    return render(request,'admin/baseadmin.html')

def camp_entry(request):
    return render(request,'camp_home.html')

def public_entry(request):
    return render(request,'public_home.html')

def volunteer_entry(request):
    return render(request,'volunteer_home.html')

def station_entry(request):
    return render(request,'station_home.html')

def login_index(request):
    if request.method == 'POST':
        form = Login2Form(request.POST)
        # print("dataaaaa",form)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = login.objects.get(email = email)
                if user.password == password:
                    if user.usertype == "camp":
                        request.session['campid'] = user.id
                        return redirect('camppage')
                    elif user.usertype == "public":
                        request.session['publicid'] = user.id
                        return redirect('publicpage')
                    elif user.usertype == "volunteer":
                        request.session['volunteerid'] = user.id
                        return redirect('volunteerpage')
                    elif user.usertype == "station":
                        request.session['stationid'] = user.id
                        return redirect('stationpage')
                else:
                    messages.error(request,'invalid password')
            except login.DoesNotExist:
                messages.error(request,'User does not exist')
    else:
        form = Login2Form()
    return render(request,'userlogin/login_index.html',{'log':form})

def campreg(request):
    if request.method == 'POST':
        form = campform(request.POST)
        login = loginform(request.POST)
        if form.is_valid() and login.is_valid():
            a=login.save(commit=False)
            a.usertype='camp'
            a.save()
            b=form.save(commit=False)
            b.login_id=a
            b.save()
        messages.success(request, 'User data saved successfully.')
        return redirect('index')
    else:
        form = campform()
        login = loginform()
        return render(request,'campregister.html',{'form':form,'log':login})

def publicreg(request):
    if request.method == 'POST':
        pub = publicform(request.POST)
        login = loginform(request.POST)
        if pub.is_valid() and login.is_valid():
            c=login.save(commit=False)
            c.usertype='public'
            c.save()
            d=pub.save(commit=False)
            d.login_id=c
            d.save()
        messages.success(request,'User data saved successfully.')
        return redirect('publicpath')
    else:
        pub = publicform()
        login = loginform()
        return render(request,'publicregister.html',{'public_form':pub,'log':login})
    
def volunteerreg(request):
    if request.method == 'POST':
        vol = volunteerform(request.POST)
        login = loginform(request.POST)
        if vol.is_valid() and login.is_valid():
            c=login.save(commit=False)
            c.usertype='volunteer'
            c.save()
            d=vol.save(commit=False)
            d.login_id=c
            d.save()
        messages.success(request,'User data saved successfully.')
        return redirect('volpath')
    else:
        vol = volunteerform()
        login = loginform()
        return render(request,'volunteerregister.html',{'vol_form':vol,'log':login})
    

def stationreg(request):
    if request.method == 'POST':
        stat = stationform(request.POST)
        login = loginform(request.POST)
        if stat.is_valid() and login.is_valid():
            c=login.save(commit=False)
            c.usertype='station'
            c.save()
            d=stat.save(commit=False)
            d.login_id=c
            d.save()
        messages.success(request,'User data saved successfully.')
        return redirect('index')
    else:
        stat = stationform()
        login = loginform()
        return render(request,'stationregister.html',{'stationf':stat,'log':login})
    
def camp_pro(request):
    log_id = request.session.get('campid')
    log = get_object_or_404(login,id = log_id)
    pro =get_object_or_404(camp,login_id = log)
    if request.method == 'POST':
        form = campform(request.POST,instance=pro)
        emailform = login_email_form(request.POST,instance=log)
        if form.is_valid() and emailform.is_valid():
            form.save()
            emailform.save()
            return redirect('camp_profile_path')
    else:
        form = campform(instance=pro)
        emailform = login_email_form(instance=log)
    return render(request,'camp_profile.html',{'camp_p':form,'emailf':emailform})

def public_pro(request):
    log_id = request.session.get('publicid')
    log = get_object_or_404(login,id = log_id)
    pro_p = get_object_or_404(public,login_id = log)
    if request.method == 'POST':
        form = publicform(request.POST,instance=pro_p)
        emailform = login_email_form(request.POST,instance=log)
        if form.is_valid() and emailform.is_valid():
            form.save()
            emailform.save()
            return redirect('public_profile_path')
    else:
        form = publicform(instance=pro_p)
        emailform = login_email_form(instance=log)
    return render(request,'public_profile.html',{'public_p':form,'emailf':emailform})

def station_pro(request):
    log_id = request.session.get('stationid')
    log = get_object_or_404(login,id = log_id)
    pro_s = get_object_or_404(station,login_id = log)
    if request.method == 'POST':
        form = stationform(request.POST,instance=pro_s)
        emailform = login_email_form(request.POST,instance=log)
        if form.is_valid() and emailform.is_valid():
            form.save()
            emailform.save()
            return redirect('station_profile_path')
    else:
        form = stationform(instance=pro_s)
        emailform = login_email_form(instance=log)
    return render(request,'station_profile.html',{'station_p':form,'emailf':emailform})

def volunteer_pro(request):
    log_id = request.session.get('volunteerid')
    log = get_object_or_404(login,id = log_id)
    pro_v = get_object_or_404(volunteer,login_id = log)
    if request.method == 'POST':
        form = volunteerform(request.POST,instance=pro_v)
        emailform = login_email_form(request.POST,instance=log)
        if form.is_valid() and emailform.is_valid():
            form.save()
            emailform.save()
            return redirect('volunteer_profile_path')
    else:
        form = volunteerform(instance=pro_v)
        emailform = login_email_form(instance=log)
    return render(request,'volunteer_profile.html',{'volunteer_p':form,'emailf':emailform})




# Create your views here.
