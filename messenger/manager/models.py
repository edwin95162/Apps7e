from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class main (models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField('Status', default=True)
    create_date = models.DateField('Creation date', auto_now=False, auto_now_add=True)
    modify_date = models.DateField('Modify date', auto_now=False, auto_now_add=True)
    delete_date = models.DateField('Delete date', auto_now=False, auto_now_add=True)
    ###.....

    class Meta: # no crea un modelo.. no se sube con makemigration y no sube a pgadmin.. de uso interno
        abstract = True

class category(main): #al poner main, esta heredando modelos de la clase main
    name = models.CharField ('Category name', max_length=100, unique=True)
    image = models.ImageField ('Category Image',upload_to= 'category/')
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(main):
        return self.name

class author(main):
    first_name =models.CharField('Fist name', max_length=100)
    last_name =models.CharField('Last name', max_length=100)
    email = models.EmailField ('E-mail', max_length=150)
    description = models.TextField ('Description')
    image = models.ImageField ('Author image', null= True, blank=True, upload_to='authors/') #null=true no es necesario poner ese dato en la inscripcion
    facebook = models.URLField ('Facebook', null= True,blank=True )
    twitter = models.URLField ('Twitter', null= True,blank=True )
    instagram = models.URLField ('Instagram', null= True,blank=True )
    web = models.URLField ('Web', null= True,blank=True )
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
    def __str__(self):
        return '{0},{1}'.format(self.first_name,self.last_name)         #concatenar = interpolar: dos valores se vuelven uno
    
class post(main):
    title = models.CharField ('Title', max_length=100, unique=True)
    slug = models.CharField ('Slug', max_length=150, unique=True)
    description = models.TextField ('Description')
    id_author = models.ForeignKey(author, on_delete=models.CASCADE) #CASCADE: para evitar basura
    id_category = models.ForeignKey(category, on_delete=models.CASCADE)
    image = models.ImageField ('Image Post', upload_to='images/', max_length=150)
    published = models.BooleanField('Published / No published', default=False)
    published_date = models.DateField('Publish date')
    content = RichTextField()
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Post'
    def __str__(self):
        return self.title           #pip install django-ckeditor: Utilizado para texto enriquecido
