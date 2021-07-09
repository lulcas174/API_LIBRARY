from core.models import Lib
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

class LibSerializer(serializers.ModelSerializer):
    class Meta:
      model = Lib
      fields = ['title','publisher','book_cover','author','id']
      Read_only_fields = ('id')