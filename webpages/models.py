from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.db import models

CLOTHING_TYPE_CHOICES = \
    [('Streetwear Style', 'Streetwear Style'), ('Ethnic fashion style ', 'Ethnic fashion style '),
     ('Formal Office Wear', 'Formal Office Wear'), ('Business Casual', 'Business Casual'),
     ('Evening Black Tie', 'Evening Black Tie'), ('Sports Wear', 'Sports Wear'),
     ('Girly Style ', 'Girly Style '), ('Androgynous fashion style', 'Androgynous fashion style'),
     ('E girl', 'E girl'), ('Scene fashion style', 'Scene fashion style'),
     ('Rocker Chic Style', 'Rocker Chic Style'), ('Skateboarders', 'Skateboarders'),
     ('Goth Fashion', 'Goth Fashion'), ('Maternity Style', 'Maternity Style'),
     ('Lolita Fashion', 'Lolita Fashion'), ('Gothic lolita style', 'Gothic lolita style'),
     ('Hip Hop Style', 'Hip Hop Style'), ('Chave culture Style', 'Chave culture Style'),
     ('Kawaii fashion', 'Kawaii fashion'), ('Preppy style', 'Preppy style'),
     ('Cowgirl fashion style', 'Cowgirl fashion style'),
     ('Lagenlook Fashion style', 'Lagenlook Fashion style'),
     ('Girl next door fashion style', 'Girl next door fashion style'),
     ('Casual Chic Style', 'Casual Chic Style'), ('Geeky chic Style', 'Geeky chic Style'),
     ('Military style', 'Military style'), ('Retro Fashion', 'Retro Fashion'),
     ('Flapper fashion (20s look),', 'Flapper fashion (20s look),'),
     ('Tomboy', 'Tomboy'), ('Garconne look', 'Garconne look'),
     ('Vacation (Resort), style', 'Vacation (Resort), style'), ('Camp Style', 'Camp Style'),
     ('Artsy Fashion style', 'Artsy Fashion style'), ('Grunge style', 'Grunge style'),
     ('Punk', 'Punk'), ('Boho/Bohemian chic', 'Boho/Bohemian chic'),
     ('Biker fashion', 'Biker fashion'), ('Psychedelic Fashion style', 'Psychedelic Fashion style'),
     ('Cosplay Fashion', 'Cosplay Fashion'), ('Haute Couture', 'Haute Couture'),
     ('Modest fashion', 'Modest fashion'), ('Prairie chic style', 'Prairie chic style'),
     ('Rave fashion', 'Rave fashion'), ('Flamboyant style', 'Flamboyant style'),
     ('Ankara Fashion Style', 'Ankara Fashion Style'),
     ('Arthoe Fashion Style', 'Arthoe Fashion Style')]

CLOTHING_METRIALS_TYPE_CHOICES = [
    ('Choice1', 'Choice1'),
    ('Choice2', 'Choice2'),
    ('Choice3', 'Choice'),
    ('Choice4', 'Choice4'),

]

CLOTHING_SIZE = [
    ("XS", "X-SMALL"),
    ("X", "SMALL"),
    ("M", "MEDIUM"),
    ("L", "LARGE"),
    ("ALL-SIZE", "ALL-SIZE")
]

ITEM_GENDER = [
    ("F", "FEMALE"),
    ("M", "MALE"),
    ("UNISEX", "UNISEX"),
    ("Kids", "KIDS")
]


def get_image_filename(instance, filename):
    """
    returns the path that contains the address of the post for the image
    """
    post = instance.post
    address = "-".join(item for item in [post.title, post.material_type, post.clothing_type] if item)
    slug = slugify(address)
    return "post_images/%s-%s" % (slug, filename)


class Post(models.Model):
    """
    this code creates a migrations, takes in the class below and creates an sql
    query
    the fields are defined below come teh model defined above
    """
    summary = models.TextField(null=True, blank=True, verbose_name="Describe your product")
    title = models.CharField(max_length=50, verbose_name="Give your ripple a title")
    material_type = models.CharField(max_length=255, verbose_name="material type",
                                     choices=CLOTHING_METRIALS_TYPE_CHOICES)
    clothing_type = models.CharField(max_length=255, verbose_name="Clothing type", choices=CLOTHING_TYPE_CHOICES)
    available_quantity = models.IntegerField(verbose_name="Available quantity", blank=True, null=False)
    quantity_weight = models.IntegerField(verbose_name="Quantity Kilograms")
    item_size = models.CharField(max_length=255, verbose_name="Item size", choices=CLOTHING_SIZE)
    item_gender = models.CharField(max_length=255, verbose_name="Gender", choices=ITEM_GENDER)
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

        the pk is used to identify each post, meaning when each post is created,
        it's assigned a pk number
        :return:
        """
        return reverse('post-detail', kwargs={'pk': self.pk})

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        """
        overwriting the django save method
        by passing in the estimated price into the price before it is saved
        """
        display_q1 = self.material_type if 46 > len(self.material_type) else (self.material_type[:45]) + ".."
        display_q2 = self.clothing_type if self.material_type is not None or 46 > len(self.clothing_type) \
            else (self.clothing_type[:45]) + ".."
        title = self.title.upper()
        self.title = title
        self.display_q1 = display_q1
        self.display_q2 = display_q2
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
