# Generated by Django 3.1.4 on 2021-01-01 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210101_1632'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Home Page', 'verbose_name_plural': 'Home Pages'},
        ),
        migrations.AddField(
            model_name='homepage',
            name='featuredPost1_author',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='featuredPost1_category',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='featuredPost1_date',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='featuredPost1_discription',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='featuredPost1_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='coverstory_discription',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
