from django import template

register = template.Library()


class IncludeNode(template.Node):
    def __init__(self, template_name):
        self.template_name = template_name

    def render(self, context):
        try:
            # Loading the template and rendering it
            included_template = template.loader.get_template(
                self.template_name).render(context)
        except template.TemplateDoesNotExist:
            included_template = ''
        return included_template


@register.tag
def try_to_include(parser, token):
    """Usage: {% try_to_include "head.html" %}

    This will fail silently if the template doesn't exist. If it does, it will
    be rendered with the current context."""
    try:
        tag_name, template_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError,\
        "%r tag requires a single argument" % token.contents.split()[0]

    return IncludeNode(template_name[1:-1])