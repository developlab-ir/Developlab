from django.views import generic
from .models import Post,Comment
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect,get_object_or_404


class BlogMainPageView(generic.TemplateView):
    template_name = "blog/main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(is_active=True)[:10]
        return context

class BlogListView(generic.ListView):
    template_name = "blog/post-list.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(is_active=True)
    
class PostDetailView(generic.DetailView):
    template_name = "blog/post-detail.html"
    context_object_name = "post"
    model = Post
    pk_url_kwarg = "pk"

    def get_queryset(self):
        query = Post.objects.filter(id=self.kwargs.get(self.pk_url_kwarg),is_active=True)
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(status="okay",reply_to__isnull=True)

        return context

class PostCreateView(LoginRequiredMixin,generic.CreateView):
    template_name = "blog/post-create-or-edit.html"
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("blog:list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin,generic.UpdateView):
    template_name = "blog/post-create-or-edit.html"
    model = Post
    form_class = PostForm
    
    success_url = reverse_lazy("blog:list")

    def dispatch(self, request, *args, **kwargs):
        query = Post.objects.filter(id=self.kwargs.get(self.pk_url_kwarg),author=request.user)
        if not query.exists():
            messages.error(request,"شما نویسنده ی این پست نیستید")
            return redirect(self.success_url)
        if query.filter(is_active=False):
            messages.error(request,"این پست در دسترس نیست")
            return redirect(self.success_url)

        return super().dispatch(request, *args, **kwargs)

class PostDeleteView(LoginRequiredMixin,generic.DeleteView):
    template_name = "blog/post-delete.html"
    model = Post
    success_url = reverse_lazy("blog:list")

    def dispatch(self, request, *args, **kwargs):
        query = Post.objects.filter(id=self.kwargs.get(self.pk_url_kwarg),author=request.user)
        if not query.exists():
            messages.error(request,"شما نویسنده ی این پست نیستید")
            return redirect(self.success_url)
        if query.filter(is_active=False):
            messages.error(request,"این پست در دسترس نیست")
            return redirect(self.success_url)

        return super().dispatch(request, *args, **kwargs)


class BlogDashboardView(LoginRequiredMixin,generic.TemplateView):
    template_name = "blog/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_cnt"] = len(Post.objects.filter(author=self.request.user)) or 0
        context["post_verify_cnt"] = len(Post.objects.filter(author=self.request.user,is_active=True)) or 0

        return context

class CommentCreateView(LoginRequiredMixin,generic.View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        description = request.POST.get("description")
        parent_id = request.POST.get("parent_comment")

        if not description:
            messages.error(request, "متن نظر نباید خالی باشد.")
            return redirect(post.get_absolute_url())

        if parent_id:
            parent = get_object_or_404(Comment,id=parent_id,post=post)
            Comment.objects.create(
                post=post,
                writer=request.user,
                description=description,
                reply_to=parent,
            )
        else:
            Comment.objects.create(
                post=post,
                writer=request.user,
                description=description,
            )

        messages.success(request, "نظر شما ثبت شد و بعد از بررسی نمایش داده می شود.")
        return redirect(post.get_absolute_url())
    