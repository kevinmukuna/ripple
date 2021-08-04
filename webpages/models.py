from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.db import models
from embed_video.fields import EmbedVideoField


def get_image_filename(instance, filename):
    """
    returns the path that contains the address of the post for the image
    """
    post = instance.post
    address = "-".join(item for item in [post.title, post.question1, post.question2, post.question3] if item)
    slug = slugify(address)
    return "post_images/%s-%s" % (slug, filename)


class Post(models.Model):
    """
    this code creates a migrations, takes in the class below and creates an sql
    query
    the fields are defined below come teh model defined above
    """
    summary = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name="Topic Of The week")
    question1 = models.CharField(max_length=255, verbose_name="Question 1")
    question2 = models.CharField(max_length=255, verbose_name="Question 2", blank=True, null=False)
    question3 = models.CharField(max_length=255, verbose_name="Question 3", blank=True, null=False)
    video = EmbedVideoField()

    date_posted = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, related_name="user_posts", on_delete=models.CASCADE)
    display_q1 = models.CharField(max_length=255, null=False, blank=True, editable=False)
    display_q2 = models.CharField(max_length=255, null=False, blank=True, editable=False)
    display_q3 = models.CharField(max_length=255, null=False, blank=True, editable=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        """
            returns the address of a post
        """
        return self.title

    def get_absolute_url(self):
        """
            this method return a string to redirect the user after posting to that
            post by returning post details the primary key of the newly created
            post

            the pk is used to identify each post, meaning when each post is creted,
            it's assigned a pk number :return:
        """
        return reverse('post-detail', kwargs={'pk': self.pk})

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        """
            overwriting the django save method
            by passing in the estimated price into the price before it is saved
        """
        display_q1 = self.question1 if 46 > len(self.question1) else (self.question1[:45]) + ".."
        display_q2 = self.question2 if self.question1 is not None or 46 > len(self.question2) else (self.question2[
                                                                                                    :45]) + ".."
        display_q3 = self.question3 if self.question1 is not None or 46 > len(self.question3) else (self.question3[
                                                                                                    :45]) + ".."

        title = self.title.upper()
        self.title = title
        self.display_q1 = display_q1
        self.display_q2 = display_q2
        self.display_q3 = display_q3

        super().save(force_insert, force_update, *args, **kwargs)


class PostImage(models.Model):
    """
    the model is used for image posting and image deletion
    """
    image = models.ImageField('images', upload_to=get_image_filename, null=True, blank=True)
    post = models.ForeignKey(Post, related_name='post_images', on_delete=models.CASCADE)

    def delete(self):
        """delete the file when the object is deleted"""
        self.image.delete()
        super(PostImage, self).delete()


# TODO create review model

"""
app from the solution 
requirement 
sustainable to be a key
supporting small business and the local community


brand image for people buying from the local store
"""