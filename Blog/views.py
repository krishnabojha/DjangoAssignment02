from django.shortcuts import render, redirect
from django.http import HttpResponse
from Blog.models import Blog, AuthorDetail
from django.contrib.auth.models import User

from .Form import BlogForm, AuthorDetailForm

# super user email : admin@gmail.com
# password : krishna
def homePage(request):
    try:
        LoggedInEmail = request.user.email
        try:
            authordata = AuthorDetail.objects.get(email=LoggedInEmail)
        except:
            AuthorDetail.objects.create(address = '', email = LoggedInEmail)
            authordata = AuthorDetail.objects.get(email=LoggedInEmail)
        context = {
            'data':authordata
        }
        if authordata.profile_img != '':
            print('profile Image : ', authordata.profile_img)
        else:
            print('no Image')
        return render(request, 'home.html', context)
    except:
        return render(request, 'home.html', context)
        # return redirect('/signin/')

def blogPage(request):
    # list of the item of the blog database
    query = Blog.objects.all()
    context = {
        'items':query
    }
    return render(request, 'bloglist.html', context)

def profilePage(request):
    # currently logged in user email
    LoggedInEmail = request.user.email
    # fetching info of logged in user from authordetail database
    Olddata = AuthorDetail.objects.get(email=LoggedInEmail)
    # fetching info of logged in user from User database
    AuthData = User.objects.get(email= LoggedInEmail)
    if request.method == 'GET':
        form = AuthorDetailForm()

        query = Blog.objects.all()

        print('Inside the get.', query)
        context = {
            'username' : AuthData.username,
            'emailAddress' : str(LoggedInEmail),
            'address' : Olddata.address,
            'items' : query
        }
        return render(request, 'ProfileDetail.html', context)
    if request.method == 'POST':
        form = AuthorDetailForm(request.POST)
        print('USER : ', User.objects.get(email= LoggedInEmail).username)
        try:
            AuthData.username = request.POST['username']
            if request.POST['ProfileImage'] != '':
                Olddata.profile_img = 'images/' + request.POST['ProfileImage']
            Olddata.address = request.POST['address']
            # uncomment below if you want to edit useremail and password as too
            # AuthData.email = request.POST['email']
            # Olddata.email = request.POST['email']
            Olddata.save()
            AuthData.save()
            return redirect('/blog/')
        except:
            return redirect('/blog/profile/')
# add new blog to the system
def writeBlog(request):
    current_email = request.user.email
    print(current_email)
    if request.method == "GET":
        return render(request, 'BlogWrite.html',{})

    if request.method == "POST":
        form = BlogForm(request.POST)
        print(request.POST)
        print(current_email)
        Blog.objects.create(title=request.POST['title'], author= request.POST['authorname'], description = request.POST['blogarea'], email = AuthorDetail.objects.get(email= current_email))
        print('saved')
        return redirect('/blog/')
# to read blog page 
def readBlog(request, pk):
    SelectedBlog = Blog.objects.get( id = pk)
    return render(request, 'ReadBlog.html', {'item' : SelectedBlog})
# to edit the personal blog data
def editBlog(request, pk):
    qs = Blog.objects.get(id = pk)
    if request.method == 'GET':
        return render(request, 'BlogWrite.html', {'blog' : qs})
    
    if request.method == 'POST':
        try:
            form = BlogForm(request.POST)
            qs.title = request.POST['title']
            qs.author = request.POST['authorname']
            qs.description = request.POST['blogarea']
            qs.save()
            return redirect("/blog/profile/")

        except:
            return render(request, 'BlogWrite.html', {'blog' : qs})


