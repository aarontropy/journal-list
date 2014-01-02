from django.db import models
from django.utils.text import slugify

class JLCategory(models.Model):
    category_text = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, unique=True)

    def __unicode__(self):
        return self.category_text

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_text)
        super(JLCategory, self).save(*args, **kwargs)


class JLItem(models.Model):
    category = models.ForeignKey(JLCategory, related_name='items')

    item_text = models.CharField(max_length=500)
    pub_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        if len(self.item_text) > 50:
            return "%s..." % self.item_text[:47]
        else:
            return self.item_text