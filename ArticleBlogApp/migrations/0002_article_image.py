# Generated by Django 4.2.4 on 2023-09-03 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArticleBlogApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
