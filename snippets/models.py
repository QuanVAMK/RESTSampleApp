from django.db import models


from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# populate the highlighted field
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# lexer = break a stream of source into tokens (semantical words) e.g.
# if,while,else or comments.

# Get all tokens (have been formatted into array of some data sturcture)
LEXERS = [item for item in get_all_lexers() if item[1]]

LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# how to highlight different token types, e.g. 'red and bold' for if-else
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Snippet(models.Model):
    # Set the timezone when instance is created
    created = models.DateTimeField(auto_now_add=True)
    # blank=True -> is not required    
    title = models.CharField(max_length=100, blank=True, default='')
    # TextField > CharField
    code = models.TextField()
    lineos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()

    # metadata = anything but a field e.g. ordering options, database table
    # name.
    class Meta:
        # sort results by value of created
        ordering = ('created',)

    def save(self, *args, **kwargs):
        '''
        Use the pygments library to create highlighted HTML
        representation of the code snippet
        '''
        lexer = get_lexer_by_name(self.language)
        lineos = self.lineos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, lineos=lineos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)

