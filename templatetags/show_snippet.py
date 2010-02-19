from django import template
from snippets.models import Snippet

register = template.Library()

@register.tag(name="show_snippet")
def show_snippet(parser, token):
    """Show a snippet from the DB"""

    try:
        tag_name, name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires a single argument" % token.contents.split()[0])

    return ShowSnippetNode(name)


class ShowSnippetNode(template.Node):
    """Show the actual snippet"""

    def __init__(self, name):
        self.name = name

    def render(self, context):
        return Snippet.objects.get_snippet(self.name)
