from rest_framework import serializers
from.models import Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['pid','pname','pcost','pmfdt','pexpdt']
    # pid=serializers.IntegerField()
    # pname=serializers.CharField(max_length=20)
    # pcost=serializers.DecimalField(max_digits=10,decimal_places=2)
    # pmfdt=serializers.DateField()
    # pexpdt=serializers.DateField()