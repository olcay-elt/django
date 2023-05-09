from rest_framework import serializers
from.models import *

class FixSerializer(serializers.ModelSerializer):
    user_id=serializers.IntegerField(read_only=True)
    user=serializers.StringRelatedField()# kullancıının ismini göster
    class Meta:
        fields='__all__'
        # fields=('fieldname',)
        #exclude

class BlogCommentSerializer(FixSerializer):
    blog_post_id=serializers.IntegerField()
    blog_post=serializers.StringRelatedField()
    class Meta(FixSerializer.Meta):
        model=BlogComment
        
class BlogPostSerializer(FixSerializer):
    blog_category_id=serializers.IntegerField()# bir üst katdın id si
    blog_category=serializers.StringRelatedField()# bir üst kaydın name i

    class Meta(FixSerializer.Meta):
        model=BlogPost

class BlogCategorySerializer(FixSerializer):
    class Meta(FixSerializer.Meta):
        model=BlogCategory



