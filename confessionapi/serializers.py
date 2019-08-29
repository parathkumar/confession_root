from rest_framework import serializers
from .models import posts

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        read_only_fields = ['pk','author']
        model = posts
        '''def save(self, **kwargs):
        user = serializers.CurrentUserDefault()
        title = self.validated_data['title']
        description = self.validated_data['description']
        content = self.validated_data['content']'''