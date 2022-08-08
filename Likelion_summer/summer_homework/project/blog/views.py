from django.shortcuts import render, redirect
from .models import Post, Like,  Comment
from .forms import PostForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

# Create your views here.


def home(request):
    posts = Post.objects.all()

    return render(request, 'blog/home.html', {'posts': posts})


def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.save()
            return redirect('blog:detail', new_post.pk)
    else:
        form = PostForm()
        context = {
            'form': form,
        }
    return render(request, 'blog/new.html', context)


def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    return render(request, 'blog/detail.html', {'post': post})


def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        Post.objects.filter(pk=post_pk).update(
            title=request.POST['title'],
            realtor=request.POST['realtor'],
            content=request.POST['content']
        )
        return redirect('blog:detail', post_pk)

    return render(request, 'blog/edit.html', {'post': post})


def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()

    return redirect('blog:home')


def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('blog:detail', post_pk)


@csrf_exempt
def like(request):
    if request.method == "POST":
        request_body = json.loads(request.body)
        post_pk = request_body["post_pk"]

        existing_like = Like.objects.filter(
            post=Post.objects.get(pk=post_pk),
            user=request.user
        )

        # 좋아요 취소
        if existing_like.count() > 0:
            existing_like.delete()

        # 좋아요 생성
        else:
            Like.objects.create(
                post=Post.objects.get(pk=post_pk),
                user=request.user
            )

    post_likes = Like.objects.filter(
        post=Post.objects.get(pk=post_pk)
    )

    my_like = Like.objects.filter(
        post=Post.objects.get(pk=post_pk),
        user=request.user
    )

    response = {
        'like_count': post_likes.count(),
        'my_like': my_like.count(),
    }

    return HttpResponse(json.dumps(response))
