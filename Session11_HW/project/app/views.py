from turtle import title
from django.shortcuts import render, redirect
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.


def list_page(request):
    posts = Post.objects.all()

    return render(request, "list_page.html", {"posts": posts})


@login_required(login_url="/registration/login")
def create_page(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        new_post = Post.objects.create(
            title=title, content=content, author=request.user
        )
        return redirect("detail_page", new_post.pk)

    return render(request, "create_page.html")


def edit_page(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        Post.objects.filter(pk=post_pk).update(title=title, content=content)
        return redirect("detail_page", post_pk)

    return render(request, "edit_page.html", {"post": post})


@login_required(login_url="/registration/login")
def detail_page(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    print(type(post.author), "post.author")
    if request.method == "POST":
        content = request.POST["content"]
        Comment.objects.create(post=post, content=content, author=request.user)

        return redirect("detail_page", post_pk)
    return render(request, "detail_page.html", {"post": post})


def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect("detail_page", post_pk)


def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect("list_page")


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        found_user = User.objects.filter(
            username=username
        )  # 이건 filter니까, 만약에 지금 입력한 username이 존재하지 않으면 반환을 안 할 테니, 아래 len에서는 0이 나올 것임. 0보다 크다는 것은 결국 똑같은 username이 있기에 반환한다는 것.
        if len(found_user):
            error = "이미 아이디가 존재합니다"
            return render(request, "registration/signup.html", {"error": error})
        new_user = User.objects.create_user(
            username=username, password=password)
        auth.login(request, new_user)
        return redirect("list_page")
    return render(request, "registration/signup.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(
                request, user, backend="django.contrib.auth.backends.ModelBackend"
            )
            # return redirect("home")
            return redirect(request.GET.get("next", "/"))
        error = "아이디 또는 비밀번호가 틀립니다"
        return render(request, "registration/login.html", {"error": error})

    return render(request, "registration/login.html")


def logout(request):
    auth.logout(request)

    return redirect("list_page")
