from django.db import models
from django.shortcuts import render

from modelcluster.fields import ParentalKey

from wagtail.api import APIField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    StreamFieldPanel,
    PageChooserPanel,
    ObjectList,
    TabbedInterface,
)
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route

from rest_framework.fields import Field

# from streams import blocks


class HomePage(RoutablePageMixin, Page):
    """Home page model."""
    template = "home/home_page.html"

    subpage_types = [
        'blog.BlogListingPage',
        # 'contact.ContactPage',
        # 'flex.FlexPage',
    ]
    parent_page_type = [
        'wagtailcore.Page'
    ]

    """ cover story"""
    coverstory_blog = models.ForeignKey(
        # 'wagtailcore.Page',
        'blog.BlogDetailPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Blog which is selected as coverstory',
        verbose_name='Coverstory blog'
    )

    """ featured post 1"""
    featuredPost1_blog = models.ForeignKey(
        # 'wagtailcore.Page',
        'blog.BlogDetailPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='First featured blog',
        verbose_name='Featured blog 1'
    )

    """ featured post 2 """
    featuredPost2_blog = models.ForeignKey(
        'blog.BlogDetailPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Second featured blog',
        verbose_name='Featured blog 2'
    )

    """ about section """
    About_section_title = models.CharField(
        max_length=50, blank=False, null=True)
    About_section_text = models.CharField(
        max_length=250, blank=False, null=True)

    blog_listing_section_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the blog section copy'
    )
    blog_listing_section = models.ForeignKey(
        # 'blog.BlogDetailPage',
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='First blog listing section for the homepage. Will display up to '
        'five child items.',
        verbose_name='Blog listing section'
    )
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            PageChooserPanel('coverstory_blog'), ], heading="Cover story"),
        MultiFieldPanel([
            PageChooserPanel('featuredPost1_blog'), ], heading="Featured Post 1"),
        MultiFieldPanel([
            PageChooserPanel('featuredPost2_blog'), ], heading="Featured Post 2"),
        MultiFieldPanel([
            FieldPanel('blog_listing_section_title'),
            PageChooserPanel('blog_listing_section'),
        ], heading="Blog list section"),
        MultiFieldPanel([
            FieldPanel('About_section_title'),
            FieldPanel('About_section_text'),
        ], heading="About Section"),
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
