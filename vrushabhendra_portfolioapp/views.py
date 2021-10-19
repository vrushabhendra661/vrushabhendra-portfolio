from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Contact

# Create your views here.

def homepage(request):
    return render(request,'index.html')

def project_mms_page(request):
    """ 
    This function returns main page of medicolitesource project.
    """
    project = "MMS ~ MEDICOLITESOURCE"
    return render(request, 'project_mms.html', {'project_name': project})

def project_instaclone_page(request):
    """ 
    This function returns main page of instagram clone project.
    """
    project = "INSTAGRAM ~ CLONE"
    return render(request, 'project_instaclone.html', {'project_name': project})

def project_ecom_page(request):
    """ 
    This function returns main page of e-commerce project.
    """
    project = "E ~ COMMERCE"
    return render(request, 'project_ecom.html', {'project_name': project})

def mywebconnect_page(request):
    """ 
    This function returns main page of connect web developent .
    """
    project = "WEB ~ DEVELOPMENT"
    return render(request, 'vrushabhendrakumarkn.html', {'work_name': project})

def insert_contactdata(request):
    """
    This function to add contact to database. 
    """
    error = ''
    error_dict = None
    if request.method == 'POST':
        sender_name = request.POST['sender-name']
        sender_email = request.POST['sender-email']
        sender_message = request.POST['message']
        if Contact.objects.filter(email=sender_email).exists():
            messages.warning(request,'ALERT: Email already exist. Try with other email !!!')
            return redirect('homepage')
        else:
            try:
                sender = Contact.objects.create(name=sender_name, email=sender_email, comment=sender_message)
                messages.success(request,'Submission is successful')
                error = 'no'
                return redirect('homepage')

            except Exception as e:
                print(e)
                error_name = type(e).__name__
                error = 'yes'
                error_dict = {'error': error, 'erron_name': error_name}
                
                return render(request, 'index.html',error_dict)