# Generated by Django 3.1.4 on 2021-01-02 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('home', '0005_auto_20210102_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='featuredPost1_image',
            field=models.ForeignKey(blank=True, help_text='fetured post 1 image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='featuredPost2_image',
            field=models.ForeignKey(blank=True, help_text='fetured post 2 image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
