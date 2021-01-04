# Generated by Django 3.1.4 on 2021-01-01 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('blog', '0009_auto_20190422_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogauthor',
            name='image',
        ),
        migrations.RemoveField(
            model_name='blogauthorsorderable',
            name='author',
        ),
        migrations.RemoveField(
            model_name='blogauthorsorderable',
            name='page',
        ),
        migrations.RemoveField(
            model_name='blogdetailpage',
            name='banner_image',
        ),
        migrations.RemoveField(
            model_name='blogdetailpage',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='blogdetailpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='blogdetailpage',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='bloglistingpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='blogpagetag',
            name='content_object',
        ),
        migrations.RemoveField(
            model_name='blogpagetag',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='videoblogpage',
            name='blogdetailpage_ptr',
        ),
        migrations.DeleteModel(
            name='ArticleBlogPage',
        ),
        migrations.DeleteModel(
            name='BlogAuthor',
        ),
        migrations.DeleteModel(
            name='BlogAuthorsOrderable',
        ),
        migrations.DeleteModel(
            name='BlogCategory',
        ),
        migrations.DeleteModel(
            name='BlogDetailPage',
        ),
        migrations.DeleteModel(
            name='BlogListingPage',
        ),
        migrations.DeleteModel(
            name='BlogPageTag',
        ),
        migrations.DeleteModel(
            name='VideoBlogPage',
        ),
    ]