from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, RedirectView

from posts.forms import AddPostMyForm, UpdatePostMyForm
from posts.models import Posts


class PostListView(ListView):
    """Список публичных публикаций"""
    model = Posts
    template_name = 'posts/posts_list.html'
    extra_context = {
        'title': 'Публикации'
    }


class PostDetailView(DetailView):
    """Детали бесплатной публичной публикации"""
    model = Posts
    template_name = 'posts/posts_detail.html'


class PostPayRedirectView(LoginRequiredMixin, RedirectView):
    """Детали платной публичной публикации"""

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy("posts:posts")


class PostMyListView(PermissionRequiredMixin, ListView):
    """Список моих публикаций"""
    model = Posts
    template_name = 'posts/posts_my_list.html'
    extra_context = {
        'title': 'Мои публикации'
    }
    permission_required = ['posts.view_posts']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['object_list'] = Posts.objects.filter(owner=self.request.user)
        return context


class PostMyDetailView(PermissionRequiredMixin, DetailView):
    """Детали публикаций"""
    model = Posts
    template_name = 'posts/posts_my_detail.html'
    permission_required = ['posts.view_posts']



class PostMyCreateView(PermissionRequiredMixin, CreateView):
    """Создание моей публикаций"""
    model = Posts
    template_name = 'posts/posts_my_form.html'
    permission_required = ['posts.add_posts']
    extra_context = {
        'title': 'Добавить публикацию'
    }
    form_class = AddPostMyForm

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class PostMyUpdateView(PermissionRequiredMixin, UpdateView):
    """Обновление контента моей публикаций"""
    model = Posts
    template_name = 'posts/posts_my_form.html'
    permission_required = ['posts.change_posts']
    form_class = UpdatePostMyForm

    def get_success_url(self):
        return reverse_lazy('posts:my_posts_detail', kwargs={'pk': self.object.pk})


class PostMyDeleteView(PermissionRequiredMixin, DeleteView):
    """Удаление моей публикаций"""
    model = Posts
    template_name = 'posts/posts_my_confirm_delete.html'
    permission_required = ['posts.delete_posts']
    success_url = reverse_lazy('posts:my_posts')
