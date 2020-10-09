from django.db import models


class CountryModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    active = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'country'


class AuthorModel(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=150)
    description = models.CharField(max_length=1500, default=None, null=True)
    country = models.ForeignKey('CountryModel', default=None, null=True, on_delete=models.DO_NOTHING)
    birth_day = models.DateField(default=None, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'author'
