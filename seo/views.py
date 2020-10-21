from django.shortcuts import render, get_object_or_404
from .models import Post,About
from django.core.mail import send_mail


# Create your views here.
def index(request):
    posts = Post.objects.all    # getting all the post data from admin
    return render(request,'index.html', {'posts':posts})   # passing the all the data to html page as arguent

def post(request, slug):
    return render(request,'post.html',{
        'post' : get_object_or_404(Post, slug=slug)
    })
def aboutus(request):
    posts = About.objects.all
    return render(request, 'about.html', {'posts':posts})

def auditform(request):

    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_url = request.POST['message-url']
        message_service = request.POST['message-service']
        message_phoneno = request.POST['message-phoneno']
        message = request.POST['message']

        #send a email
        info = "Name" + message_name +'\n'+ "email" +message_email +'\n' + "Service " +message_service+'\n' + "message" + message +'\n'+ "Phone:NO" +message_phoneno
        send_mail(
            'Visited by: '+ message_name,#subject
            info, # message
            message_email,# from email
            ['royal.nitishkaushal@gmail.com','nk512691@gmail.com','raghavkaushal155@gmail.com'],# To email
        )




        return render(request, 'freeaudit.html', {'message_name':message_name})


    else:

        return render(request, 'freeaudit.html')

def seopage(request):
    return render(request, 'seopage.html')
def ppc(request):
    return render(request, 'ppc.html')
def smo(request):
    return render(request, 'smo.html')
def amazonseo(request):
    return render(request, 'amazonseo.html')
