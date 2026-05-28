from django.shortcuts import render, redirect
from django.http import HttpRequest

# Create your views here.
users: list = []
id:int = 0

def portfolio(request:HttpRequest):
    context:dict = {
        'name': 'Kuntal Pal',
        'role': 'R&D',
        'bio': 'Passionate about building elegant with Python and Django and AI.',
        'skills': ['HTML','CSS','Python', 'Django', 'DSA', 'ML'],
        'email': 'kuntal.pal7550@gmail.com',
        'github': 'github.com/KUNTALinGITHUB',
    }

    return render(request,'profiles/portfolio.html', context)

def add_user_profile(request: HttpRequest):
    alert:str=""
    global users,id
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        city = request.POST.get("city")
        id += 1
        if name and email and city :
            if users:
                for user in users:
                    if user[1] == name:
                        alert="duplicate"
                        break
                else:
                    users.append([id,name,email,city])
                    alert="appended"
            else:
                users.append([id,name,email,city])
                alert="appended"
        else:
            alert="failed"
    context:dict = {
        "alert":alert,
        "users":users
    }

    return render(request, 'profiles/profile.html', context)

def user_profile(request:HttpRequest, name:str):
    global users
    user:list =[]
    alert:str = ""
    for i in users:
        if i[1] == name:
            user = i
            break
    else:
        alert = "not found"
    
    context:dict = {
        "name":name,
        "alert": alert,
        "user": user
    }
    return render(request, 'profiles/user_profile.html', context)