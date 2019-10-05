from django.db import models
from ckeditor.fields import RichTextField  ##texto enriquecido para HTML

# Create your models here.
class main (models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField('Status', default=True)
    create_date = models.DateField('Creation date', auto_now=False, auto_now_add=True)
    modify_date = models.DateField('Modify date', auto_now=False, auto_now_add=True)
    delete_date = models.DateField('Delete date', auto_now=False, auto_now_add=True)
    ###..... registros a utlilizar en otra tabla

    class Meta: # no crea un modelo.. no se sube con makemigration y no sube a pgadmin.. de uso interno
        abstract = True

class category(main): #al poner main, esta heredando modelos de la clase main
    name = models.CharField ('Category name', max_length=100, unique=True)
    image = models.ImageField ('Category Image',upload_to= 'category/')
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name

class author(main):
    first_name =models.CharField('Fist name', max_length=100)
    last_name =models.CharField('Last name', max_length=100)
    email = models.EmailField ('E-mail', max_length=150)
    description = models.TextField ('Description')
    image = models.ImageField ('Author image', null= True, blank=True, upload_to='authors/') #null=true no es necesario poner ese dato en la inscripcion // pillow instalar: imagenes renderizadas
    facebook = models.URLField ('Facebook', null= True,blank=True )
    twitter = models.URLField ('Twitter', null= True,blank=True )
    instagram = models.URLField ('Instagram', null= True,blank=True )
    web = models.URLField ('Web', null= True,blank=True )
    age = models.CharField('Age', max_length=2)
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
    def __str__(self):
        return '{0}{1}{2}'.format(self.first_name," ",self.last_name)         #concatenar = interpolar: dos valores se vuelven uno, se agrega espacio
    
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

class web(main):
    about_us = models.TextField ('About us')
    phone = models.CharField('Phone', max_length=20)
    email = models.EmailField('E-mail', max_length=150)
    address = models.CharField('Address', max_length=200)
    class Meta:
        verbose_name = 'Web'
        verbose_name_plural = 'Webs'
    def __str__ (self):
        return self.about_us
    
class social (main):
    facebook = models.URLField('Facebook')
    twitter = models.URLField('Twitter')
    instagram = models.URLField('Instagram')
    web = models.URLField('Web')
    class Meta:
        verbose_name = 'Social network'
        verbose_name_plural = 'Social Networks'
    def __str__ (self):
        return self.facebook

class contact (main):
    first_name = models.CharField('First name', max_length=100)
    last_name = models.CharField('Last name', max_length=100)
    email = models.EmailField('E-mail', max_length=150)
    subject = models.CharField('Subject', max_length=100)
    message = models.TextField('Message')
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
    def __str__ (self):
        return self.subject

class suscriber(main):
    email = models.EmailField('E-mail', max_length=150)
    class Meta:
        verbose_name = 'Suscriber'
        verbose_name_plural = 'Suscribers'
    def __str__ (self):
        return self.email


