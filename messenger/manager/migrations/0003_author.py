# Generated by Django 2.2.5 on 2019-10-01 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20191001_0144'),
    ]

    operations = [
        migrations.CreateModel(
            name='author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Creation date')),
                ('modify_date', models.DateField(auto_now_add=True, verbose_name='Modify date')),
                ('delete_date', models.DateField(auto_now_add=True, verbose_name='Delete date')),
                ('first_name', models.CharField(max_length=100, verbose_name='Fist name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last name')),
                ('email', models.EmailField(max_length=150, verbose_name='E-mail')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='authors/', verbose_name='Author image')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('web', models.URLField(blank=True, null=True, verbose_name='Web')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
    ]
