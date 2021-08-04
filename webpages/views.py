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
    'video',
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
    paginate_by = 5


class UserPostListView(LoginRequiredMixin, ListView):
    """
        model: name of model, in this case post
        template_name: name of templates, in this case user_posts.html
        context_object_name: name of the object u want in the template in this case posts'
        paginate_by: how many post you want in each page, in this case 5

    """
    model = Post
    template_name = 'dashboard/dashboard_post.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """
            this function get the user if they exist else it returns 404 --> this function is used to filter and display
            a requested user
            filter by the user requested and sort by the latest post
        """
        return Post.objects.filter(author=self.request.user).order_by('-date_posted')


class PostDetailView(DetailView, FormMixin):
    """
    detail view, as as above but just using the generic django conventions
    <appname>/<model>_<viewtype>.html
    eg. how it looks
    blog/post_detail.html
    """

    """fix this to render properly """
    model = Post

    # template_name = "webpages/post_detail.html"
    # data = CommentForm()

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(PostDetailView, self).form_valid(form)


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    post creation view, it requires the user to be login
    model type(as defined in the model file), in this case Post class
    fields: as define in the model, in this case POST_FIELDS
    """
    model = Post

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


# def post_detail(request, year, month, day, post):
#     # co oparate this with the one above
#     post = get_object_or_404(Post, slug=post,
#                              status='published',
#                              publish__year=year,
#                              publish__month=month,
#                              publish__day=day)
#
#     # List of active comments for this post
#     comments = post.comments.filter(active=True)
#
#     new_comment = None
#
#     if request.method == 'POST':
#         # A comment was posted
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.post = post
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#     return render(request,
#                   'blog/post/detail.html',
#                   {'post': post,
#                    'comments': comments,
#                    'new_comment': new_comment,
#                    'comment_form': comment_form})
