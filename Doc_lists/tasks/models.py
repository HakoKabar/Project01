from statistics import mode
from django.db import models
from django.utils.text import slugify

# Create your models here.
class Collection(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField()

    @classmethod
    def get_defaut_collection(cls) :
        collection,_=cls.objects.get_or_create(name="Defaut",slug="_defaut")
        return collection
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs ) :
        self.slug=self.slug or slugify(self.name)
        super().save(*args,**kwargs)

                
class Task(models.Model):
    description=models.CharField(max_length=200)
    collection=models.ForeignKey(Collection,on_delete=models.CASCADE)
    def __str__(self):
        return self.description
