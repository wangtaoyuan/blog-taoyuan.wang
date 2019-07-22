from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from datetime import datetime
from django.template.loader import get_template
from django.shortcuts import redirect

# Create your views here.


def homepage(request):
    # posts = Post.objects.all()
    # post_lists = list()
    # for count, post in enumerate(posts):
    #     post_lists.append("No.{}:".format(str(count)) + str(post) + "<br>")
    #     post_lists.append("<small>" + str(post.body) + "</small><br><br>")

    template = get_template('first.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)


def showpost(request, author):
    template = get_template('post.html')
    try:
        post = Post.objects.get(author=author)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/') #直接返回首页


def profile(request):
    return render(request, "profile.html")
