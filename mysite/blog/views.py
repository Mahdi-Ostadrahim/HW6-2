from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from blog.models import Post
# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    posts = Post.objects.filter(status=1)
    #post = get_object_or_404(posts, pk=pid)
    #context = {'post': post}
    pre = posts[0]
    found = False
    after = get_object_or_404(posts, pk=pid)
    for post in posts:
        if found:
            after = post
            break
        if post.id == pid:
            found = True
        else:
            pre = post
    post = get_object_or_404(posts, pk=pid)
    context = {'post': post, 'pre': pre, 'after': after}
    return render(request, 'blog/blog-single.html',context)

def test(request,pid):
    #post = Post.objects.get(id=pid)
    post = get_object_or_404(Post, pk=pid)
    context = {'post': post}
    return render(request,'test.html',context)