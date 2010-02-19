from django.db import models
import markdown

class SnippetManager(models.Manager):

    def get_snippet(self, name):
        """Return a snippet or silently fail if one doesn't exist"""

        try:
            snippet = self.get(name=name)

            if snippet.markdown:
                return markdown.markdown(snippet.value)

            return snippet.value

        except Snippet.DoesNotExist:
            pass

        return ""
    
class Snippet(models.Model):
    """A snippet is a piece of arbitrary text with a key. This is useful for
    storing random pieces of information in the database that we don't want
    to store in the template"""

    name = models.CharField(max_length=255, unique=True)
    value = models.TextField(blank=True, null=True)

    markdown = models.BooleanField(default=True)

    objects = SnippetManager()

    def __unicode__(self):
        return self.name
