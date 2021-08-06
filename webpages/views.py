from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from authentication.models import User

from .models import Post, PostImage

POST_FIELDS = [
    'title',
    'material_type',
    'clothing_type',
    'item_size',
    'item_gender',
    'available_quantity',
    'quantity_weight',
    'summary',

]


# Create your views here.
def aboutfunction(request):
    """
    render the specified template
    """
    return render(request, 'webpages/about.html', {'title': 'About'})


@login_required(login_url='/login/')
def dashboardfunction(request, **kwargs):
    """
        this function will display the average  selling price, estimated price and how much your properties worth
        this is displayed on the top in dashboard just below search menu

        month_price --> get the sum of estimated price of a specific user
        average_average --> average estimated price of a specific user posts
        assert_properties -->  sum of estimated prices

        if a user has no post return zeros else do the calculations and return the matrices and render it to the site
    """
    user = User.objects.get(username=request.user)
    post_count = float(Post.objects.count())
    print(post_count)
    value1 = {}
    value2 = {}
    value3 = {}
    value = {}

    value = {
        "value1": value1,
        "value2": value2,
        "value3": value3,
        "value4": 0
    }

    return render(request, 'dashboard/dashboard.html', value)


@login_required(login_url='/login/')
def dashboard_user_functionality(request):
    """
        render the specified template
    """
    return render(request, 'dashboard/all_user_function.html')


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


class UserPostListView(LoginRequiredMixin,ListView):
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
