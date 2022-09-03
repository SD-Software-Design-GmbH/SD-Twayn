from django.template import Library

from ..tools.gitlabCache import loadWikiPage
from .prettify import translateDescriptions
import markdown as md
import re

register = Library()

@register.filter()
def markdown(value):

    customTranslations = {
        "(^<p>|</p>$)": "",
        "\[ \]": '<input type="checkbox" disabled>',
        "\[x\]": '<input type="checkbox" checked disabled>'
    }

    text = translateDescriptions(md.markdown(value))
    for key,value in customTranslations.items():
        text = re.sub(key,value,text)

    return text

@register.simple_tag
def wikicontent(slug,localProject, remoteProject):
    return markdown(loadWikiPage(localProject, remoteProject, slug).content).replace('\n','<br>')