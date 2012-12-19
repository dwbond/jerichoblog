# Create your views here.

from blog.models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.template import RequestContext

import time
from calendar import month_name

def mkmonth_lst():
    """Make a list of months to show archive links."""
    print "hello"
    if not Blog.objects.count():
        print "hello"
        return []

    #set up vars
    year, month = time.localtime()[:2]
    first = Blog.objects.order_by("posted")[0]
    fyear = first.posted.year
    fmonth = first.posted.month
    months = []

    # loop over years and months
    for y in range(year, fyear-1, -1):
        start, end = 12, 0
        if y == year: start = month
        if y == fyear: end = fmonth-1

        for m in range(start, end, -1):
            months.append((y, m, month_name[m]))
    print months
    return months

def month(request, year, month):
    """Monthly archive."""

    blogs = Blog.objects.filter(posted__year=year, posted__month=month)
   
    paginator = Paginator(blogs, 4)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        blogs = paginator.page(page)
    except (InvalidPage, EmptyPage):
        blogs = paginator.page(paginator.num_pages)

    return render_to_response("archive.html", {
        'user' : request.user,
        'categories': Category.objects.all(),
        'post_list' : blogs.object_list,
        'months' : mkmonth_lst(),
        'posts' : blogs,
        'month' : month_name[int(month)],
        'year' : year,
    }, 
    context_instance = RequestContext(request),
    )

def index(request):

    blogs = Blog.objects.all().order_by("-posted")
    paginator = Paginator(blogs, 4)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        blogs = paginator.page(page)
    except (InvalidPage, EmptyPage):
        blogs = paginator.page(paginator.num_pages)

    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts' : blogs,
        'user' : request.user,
        'months': mkmonth_lst(),
        'post_list' : blogs.object_list,
    },
    context_instance = RequestContext(request),
    )

import random
def sing_a_song():
    song = ["Joshua fought the battle of Jericho", "Joshua fought the battle of Jericho", "And the wall came tumbling down", "You may talk about your men of Gideon", "You may talk about your men of Saul", "But there's none like good old Joshua", "At the battle of Jericho", "Right up to the walls of Jericho", "They marched with spear in hand", "Go blow them ram horns, Joshua cried", "'Cause the battle is in my hand", "Then the lamb, ram, sheep horns began to blow", "And the trumpets began to sound", "Joshua commanded the children to shout", "That morning Joshua fought the battle of Jericho", "Joshua fought the battle of Jericho", "And the walls came tumbling down"]
    return random.choice(song)

def view_post(request, slug):
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug),
        'categories': Category.objects.all(),
        'months' : mkmonth_lst(),
        'song_lyrics' : sing_a_song(),
    },
    context_instance = RequestContext(request),
    )

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'categories' : Category.objects.all(),
        'posts': Blog.objects.filter(category=category)[:5],
        'song_lyrics' : sing_a_song(),
    },
    context_instance = RequestContext(request),    
    )
