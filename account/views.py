from django.shortcuts import render,redirect
from django.http import HttpResponse
from account.models import User
from django.contrib import messages
from django.contrib.auth import authenticate ,login,logout
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.template import RequestContext
from django.utils.html import strip_tags

# Create your views here.

def handleSignup(request):
    if request.method == 'POST':
        #Get teh post parameters
        
        fname=request.POST['fname']
        lname=request.POST['lname']
        mobile=request.POST['mobile']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        print(email)
        #send mail 
        subject="test email"
        context = {
            'name': fname, 
            'email': email, 
            'num': mobile
        }
        
        message = render_to_string('msg.html', context)
        new_message = strip_tags(message)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]

        send_mail(subject,new_message , email_from , recipient_list,fail_silently=False,)
        
        #send email
        # subject = 'TEst Email'
        # context = {
        #     'name': fname, 
        #     'email': email, 
        #     'num': mobile
        # }
        

        print(recipient_list)


        if pass1 != pass2:
            messages.error(request, 'password dose not match')
            return redirect('handleSignup')
        
        myuser = User.objects.create_user(email,pass1)
        
        myuser.first_name =fname
        myuser.last_name =lname
        myuser.mobile = mobile
        myuser.save()
      
        messages.success(request, "Profile details updated.")
        
        return redirect('handleSignup')

    return render(request ,'signup.html')

def index(request):
    # print("................................................................")
    # print("your email is : ",request.session.get('email'))
    request.session.modified = True
    return render(request ,'home.html')


def handlelogin(request):

    if request.method == 'POST':
        loginemail = request.POST['loginemail']
        loginpass = request.POST['loginpass']

        user = authenticate(email=loginemail, password=loginpass)

        if user is not None:
            request.session['email']=user.email
            request.session['password']=user.password
            login(request, user)
            messages.success(request, "Login successful")
            return redirect('index')
        else:
            messages.error(request, "Invalid Details")
            return redirect('index')

    return render(request ,'login.html')
    # return HttpResponse("404 Error")

# Create your views here.


def showusers(request):
    user = User.objects.all()

    print("ssssssssssssssssssssssssssssssssssssssssssssssssssssssss") 
    for u in user:
        print(u.username)
        print(u.first_name )
    
    return render(request, 'showuser.html', {'user':user})


def handlelogout(request):
    logout(request)
    messages.success(request, 'Logout successfully')
    return redirect('index')




def delete_data(request,id):
    ddata= User.objects.get(id=id)
    ddata.delete()
    return redirect('showusers')

def update_data(request,id):
    udata = User.objects.get(id=id)
    # print(udata.first_name

    if request.method == 'POST':

        fname = request.POST.get('fname','')
        mobile = request.POST.get('mobile','')
        email = request.POST.get('email','')
        age = request.POST.get('age','')

        newage =  datetime.datetime.strptime(age,'%b %d, %Y').date()
        nage = newage.strftime('%Y-%m-%d')

        udata.fname = fname
        udata.mobile = mobile
        udata.email = email
        udata.age = nage

        udata.save()
        return redirect('showusers')

    return render(request, 'update.html', {'udata': udata})