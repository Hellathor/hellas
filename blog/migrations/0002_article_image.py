# Generated by Django 4.0.6 on 2022-11-17 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, upload_to='blog', verbose_name='文章封面图片, 350*232.97px'),
        ),
    ]
