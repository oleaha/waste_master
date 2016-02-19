from rest_framework import serializers
from apps.api.models import ContainerReading


class ContainerReadingSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    container = serializers.PrimaryKeyRelatedField(read_only=True)
    datetime = serializers.DateTimeField(read_only=True)
    value = serializers.IntegerField(required=True)

    '''
    Create and return a new container reading
    '''
    def create(self, validated_data):
        return ContainerReading.objects.create(**validated_data)

    '''
    Update and return an existing container reading
    '''
    def update(self, instance, validated_data):
        instance.value = validated_data.get('value', instance.value)
        instance.save()
        return instance


'''
More simple class than the one over
'''


class ContainerReadingModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContainerReading
        fields = ('id', 'container', 'datetime', 'value')
