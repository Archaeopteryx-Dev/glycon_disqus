from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

from glycon.models import BaseBlock
from .views import disqus_block_html


class DisqusBlock(BaseBlock):
    disqus_username = models.CharField(max_length=255)

    @property
    def content(self):
        return disqus_block_html(self.disqus_username)

    def __str__(self):
        return self.name

    class Data:
        description = "Add Disqus Comments"