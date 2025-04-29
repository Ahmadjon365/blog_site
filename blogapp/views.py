from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView  #, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 10
    template_name = 'blog/post/list.html'

def post_list(request, year, month, day, slug):
    post = get_object_or_404(Post, status='published', publish__year=year,
                             publish__month=month, publish__day=day, slug=slug)
    return render(request, 'blog/post/detail.html', {'post': post})
