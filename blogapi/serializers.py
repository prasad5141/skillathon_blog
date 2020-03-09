from rest_framework import serializers

from blogapp.models import Article

class GetArticlesSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Article
        fields = ('title', 'content', 'user')

    def get_user(self, instance):
        username = instance.posted_by.username
        return username


class CreateArticleSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    content = serializers.CharField(required=True)

    class Meta:
        fields = ('title', 'content')


class CreateUser(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        fields = ('username', 'password')
