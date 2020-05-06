from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Group
from .forms import PostForm


def index(request):
    latest = Post.objects.order_by("-pub_date")[:10]
    return render(request, "index.html", {"posts": latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.group_posts.order_by("-pub_date")[:12]
    return render(request, "group.html", {"group": group, "posts": posts})


def new_post(request):
    if request.method == "POST":
        form_for_new_posts = PostForm(request.POST)
        if form_for_new_posts.is_valid():
            form = form_for_new_posts.save(commit=False)
            form.author_id = request.user.pk
            form.save()
            return redirect("index")

    form = PostForm()
    return render(request, "new.html", {"form": form})
