from django.db import models


class Publishing_HouseModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)   # , auto_created=True)
    active = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'publishing_house'
        ordering = ('name',)


class CategoryModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    active = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        ordering = ('name',)


class BookModel(models.Model):
    id = models.AutoField(primary_key=True)
    image_link = models.URLField(default=None, null=True, blank=True)
    name = models.CharField(max_length=150)
    price = models.FloatField(default=None, null=True)
    description = models.CharField(max_length=500)
    publishing_house = models.ForeignKey('book.Publishing_houseModel', on_delete=models.CASCADE)
    publish_year = models.DateField()
    category = models.ForeignKey('CategoryModel', on_delete=models.CASCADE)
    count = models.IntegerField(default=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ManyToManyField('author.AuthorModel')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'books'
        ordering = ('-created',)
