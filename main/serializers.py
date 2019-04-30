from rest_framework.serializers import ModelSerializer
from .models import *
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


#Category