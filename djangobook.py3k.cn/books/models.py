from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, verbose_name = 'e-mail')

    def __unicode__(self):
        return u'%s %s' %(self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=150)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)  #https://www.cnblogs.com/phyger/p/8035253.html
    publication_date = models.DateField()  # cannot blank

    def __unicode__(self):
        return self.title
