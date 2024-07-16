from rest_framework import serializers
from .models import Person, Company

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    description_points = serializers.JSONField()

    class Meta:
        model = Company
        fields = '__all__'

    def create(self, validated_data):
        description_points = validated_data.pop('description_points')
        company = Company.objects.create(**validated_data)
        company.set_description_points(description_points)
        company.save()
        return company

    def update(self, instance, validated_data):
        description_points = validated_data.pop('description_points')
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.date = validated_data.get('date', instance.date)
        instance.location = validated_data.get('location', instance.location)
        instance.position_title = validated_data.get('position_title', instance.position_title)
        instance.description = validated_data.get('description', instance.description)
        instance.set_description_points(description_points)
        instance.save()
        return instance
