# convert complex data like model instances/query sets -> native python data
# types -> content types like JSON/XML and vice versa.

from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

# ModelSerializer automatically determine set of fields.
# Simple default implementation of create() & update()
class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')    
    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'title',
                  'code', 'lineos', 'language', 'style', 'owner')


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')
