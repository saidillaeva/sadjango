from django.shortcuts import render
from blog.models import Post

def post_view(request):
    if request.method == "GET":
        post = Post.objects.all()
        return render(request, 'post.html', {"post_key":post})
