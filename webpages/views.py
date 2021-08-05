from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin

from .models import Post, PostImage

POST_FIELDS = [
    'title',
    'question1',
    'question2',
    'question3',
    'summary',
]


# Create your views here.
def aboutfunction(request):
    """
    render the specified template
    """
    return render(request, 'webpages/about.html', {'title': 'About'})


class PostListView(ListView):
    """
    this is a list view similar to the class above, --> does the same thing as the above but more efficient as it
    handles a lot of forms work that you have to manual configure when uisng funtional views
    but passing different path names compare the convention formats--><appname>/<model>_<viewtype>.html
    """
    model = Post
    template_name = 'webpages/home.html'
    context_object_name = 'posts'
    # ordering = ["-date_posted"]
    paginate_by = 6


class PostDetailView(DetailView):
    """
    detail view, as as above but just using the generic django conventions
    <appname>/<model>_<viewtype>.html
    eg. how it looks
    blog/post_detail.html
    """

    """fix this to render properly """
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    post creation view, it requires the user to be login
    model type(as defined in the model file), in this case Post class
    fields: as define in the model, in this case POST_FIELDS
    """
    model = Post
    fields = POST_FIELDS

    def form_valid(self, form):
        """ this function allows user to create a new post if they login """
        form.instance.author = self.request.user
        self.object = form.save()
        if self.request.POST:
            for file in self.request.FILES.getlist('post_images'):
                img = PostImage(post=self.object, image=file)
                img.save()
            if form.is_valid():
                form.save()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    same as above, the only difference is we delete the
    current images before updating new images
    """
    model = Post
    fields = POST_FIELDS

    def form_valid(self, form):
        """this function ensure that a user can only  update if they are login"""
        form.instance.author = self.request.user
        p = form.save()
        if self.request.POST:
            # remove relations of all old images of the post and attach new images
            # it also delete the file itself
            if self.request.FILES.getlist('post_images'):
                for images in p.post_images.all():
                    images.delete()
                for file in self.request.FILES.getlist('post_images'):
                    img = PostImage(post=p, image=file)
                    img.save()
        return super().form_valid(form)

    def test_func(self):
        """this function ensures that only the user who post a comment can edit --> this use the UserPassesTestMixin """

        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
        delete view, delete  the post if the user that makes that request is the author
        this test_func() function ensures that only the user who posted it can edit it
         --> this use the UserPassesTestMixin

    """
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
