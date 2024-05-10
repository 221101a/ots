from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from online_test.models import *
from django.views.decorators.csrf import csrf_exempt #include this 
import random
def welcome(request):
    template=loader.get_template("welcome.html")
    res=template.render()
    return HttpResponse(res)

def signup(request):
    template=loader.get_template("signup.html")
    res=template.render()
    return HttpResponse(res)

@csrf_exempt # include  this
def store_user(request):
    if request.method=='POST':
        username=request.POST['username']
        if(len(User.objects.filter(username=username))):
            msg='username already taken ....try another username'
            context={
                'msg':msg
            }
            template=loader.get_template("signup.html")
            res=template.render(context,request)
            return HttpResponse(res)
        else:
            user=User() # insertion
            user.username=username
            user.password=request.POST['password']
            user.name=request.POST['name']
            user.save()
            template=loader.get_template("login.html")
            res=template.render()
            return HttpResponse(res)
    else:
        msg='invalid request......first signup'
        context={
            'msg':msg
        }
        template=loader.get_template("signup.html")
        res=template.render(context,request)
        return HttpResponse(res)
    
@csrf_exempt # include  this
def login(request): #authentication
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if(len(User.objects.filter(username=username))):
            user=User.objects.filter(username=username)
            if(len(user.filter(password=password))):
                request.session['username']=username # login success then ...
                user_data=User.objects.filter(username=username)
                profile_data=Profile.objects.filter(username=username)
                context={
                    'user_data':user_data,
                    'profile_data':profile_data
                }
                template=loader.get_template("homepage.html")
                res=template.render(context,request)
                return HttpResponse(res)
            else:
                msg='incorrect password.......login again'
                context={
                    'msg':msg
                }
                template=loader.get_template("login.html")
                res=template.render(context,request)
                return HttpResponse(res)
        else:
            msg='incorrect username........login again'
            context={
                'msg':msg
            }
            template=loader.get_template("login.html")
            res=template.render(context,request)
            return HttpResponse(res)
    else:
        template=loader.get_template("login.html")
        res=template.render()
        return HttpResponse(res)

def homepage(request):
    if 'username' not in request.session.keys(): 
        template=loader.get_template("welcome.html")
        res=template.render()
        return HttpResponse(res)
    else:
        username=request.session['username']
        user_data=User.objects.filter(username=username)
        profile_data=Profile.objects.filter(username=username)
        context={   
            'user_data':user_data,
            'profile_data':profile_data
        }
        template=loader.get_template("homepage.html")
        res=template.render(context,request)
        return HttpResponse(res)

def profile(request):
    template=loader.get_template("profile.html")
    res=template.render()
    return HttpResponse(res)

@csrf_exempt # include  this
def profile_save(request):
    if request.method=='POST':
        username=request.session.get('username')
        if(len(User.objects.filter(username=username))):
            profile=Profile() #insertion
            profile.username=User.objects.get(username=username)
            profile.fathers_name=request.POST['father_name']
            profile.mothers_name=request.POST['mother_name']
            profile.phone=request.POST['phone']
            profile.email=request.POST['email']
            profile.address=request.POST['address']
            profile.save()
            user_data=User.objects.filter(username=username)
            profile_data=Profile.objects.filter(username=username)
            context={
                'user_data':user_data,
                'profile_data':profile_data
            }
            template=loader.get_template("homepage.html")
            res=template.render(context,request)
            return HttpResponse(res)
        else:
            msg='incorrect username ,profile not updated'
            context={
                'msg':msg
            }
            template=loader.get_template("profile.html")
            res=template.render(context,request)
            return HttpResponse(res)
    else:
        template=loader.get_template("welcome.html")
        res=template.render()
        return HttpResponse(res)

def subject1(request):
    ques=Test_paper_subject1.objects.all()
    quse_list=list(ques)
    random.shuffle(quse_list)
    quse_list=quse_list[:4:1] ###### total questions can be customized
    context={
        'quse_list':quse_list
    }
    template=loader.get_template("subject1.html")
    res=template.render(context,request)
    return HttpResponse(res)

@csrf_exempt # include  this
def result1(request):
    if request.method=='POST':
        subject='DBMS'
        correct=0
        total=4
        for i in range(1,7,1): # traverse total number of questions
            if ('id'+str(i)) in request.POST.keys():  
                q_id=request.POST['id'+str(i)]
                ans=request.POST['option'+str(i)]
                ques=Test_paper_subject1.objects.filter(q_id=q_id)
                if(len(ques.filter(ans=ans))):
                    correct=correct+1
        wrong=total-correct
        percentage=(correct/total)*100
        username=request.session.get('username')
        history=Test_history()
        history.subject=subject
        history.username=User.objects.get(username=username)
        history.total=total
        history.correct=correct
        history.wrong=wrong
        history.percentage=percentage
        history.save()
        context={
            'total':total,
            'correct':correct,
            'wrong':wrong,
            'percentage':percentage
        }
        template=loader.get_template("result1.html")
        res=template.render(context,request)
        return HttpResponse(res)
    else:
        template=loader.get_template("welcome.html")
        res=template.render()
        return HttpResponse(res)
    
def subject2(request):
    ques=Test_paper_subject2.objects.all()
    quse_list=list(ques)
    random.shuffle(quse_list)
    quse_list=quse_list[:4:1] ###### total questions can be customized
    context={
        'quse_list':quse_list
    }
    template=loader.get_template("subject2.html")
    res=template.render(context,request)
    return HttpResponse(res)

@csrf_exempt # include  this
def result2(request):
    if request.method=='POST':
        subject='OS'
        correct=0
        total=4
        for i in range(1,7,1): # traverse total number of questions
            if ('id'+str(i)) in request.POST.keys():  
                q_id=request.POST['id'+str(i)]
                ans=request.POST['option'+str(i)]
                ques=Test_paper_subject2.objects.filter(q_id=q_id)
                if(len(ques.filter(ans=ans))):
                    correct=correct+1
        wrong=total-correct
        percentage=(correct/total)*100
        username=request.session.get('username')
        history=Test_history()
        history.username=User.objects.get(username=username)
        history.subject=subject
        history.total=total
        history.correct=correct
        history.wrong=wrong
        history.percentage=percentage
        history.save()
        context={
            'total':total,
            'correct':correct,
            'wrong':wrong,
            'percentage':percentage
        }
        template=loader.get_template("result2.html")
        res=template.render(context,request)
        return HttpResponse(res)
    else:
        template=loader.get_template("welcome.html")
        res=template.render()
        return HttpResponse(res)
    
def subject3(request):
    ques=Test_paper_subject3.objects.all()
    quse_list=list(ques)
    random.shuffle(quse_list)
    quse_list=quse_list[:4:1] ###### total questions can be customized
    context={
        'quse_list':quse_list
    }
    template=loader.get_template("subject3.html")
    res=template.render(context,request)
    return HttpResponse(res)

@csrf_exempt # include  this
def result3(request):
    if request.method=='POST':
        subject='CN'
        correct=0
        total=4 #total number of questions displayed on subject3.html
        for i in range(1,7,1): # traverse total number of questions
            if ('id'+str(i)) in request.POST.keys():  
                q_id=request.POST['id'+str(i)]
                ans=request.POST['option'+str(i)]
                ques=Test_paper_subject3.objects.filter(q_id=q_id)
                if(len(ques.filter(ans=ans))):
                    correct=correct+1
        wrong=total-correct
        percentage=(correct/total)*100
        username=request.session.get('username')
        history=Test_history()
        history.username=User.objects.get(username=username)
        history.subject=subject
        history.total=total
        history.correct=correct
        history.wrong=wrong
        history.percentage=percentage
        history.save()
        context={
            'total':total,
            'correct':correct,
            'wrong':wrong,
            'percentage':percentage
        }
        template=loader.get_template("result3.html")
        res=template.render(context,request)
        return HttpResponse(res)
    else:
        template=loader.get_template("welcome.html")
        res=template.render()
        return HttpResponse(res)

def test_history(request):
    username=request.session.get('username')
    history=Test_history.objects.filter(username=username)
    context={
        'history':history
    }
    template=loader.get_template("test_history.html")
    res=template.render(context,request)
    return HttpResponse(res)

def logout(request):
    del request.session['username'] #must destroy session keys
    template=loader.get_template("welcome.html")
    res=template.render()
    return HttpResponse(res)

def aboutUs(request):
    template=loader.get_template("about.html")
    res=template.render()
    return HttpResponse(res)