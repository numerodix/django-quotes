from os.path import abspath
from os.path import basename
from os.path import join
import random

from django import template

register = template.Library()


LINES = open(
    join(basename(abspath(__file__)), '..', 'data', 'quotes.dat')
).readlines()

@register.simple_tag
def get_random_quote():
    line_num = random.randint(0, len(LINES) / 2 - 1)
    line_num *= 2

    html = '%s<br/><em>%s</em>' % (LINES[line_num], LINES[line_num+1])
    return html
