from rest_framework import serializers
from NearBeach.models import *


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = customer
        fields = '__all__'

class OrganisationSerializer(serializers.ModelSerializer):

    class Meta:
        model = organisation
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = project
        fields = '__all__'

class QuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = quote
        fields = '__all__'

class RequestForChangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = request_for_change
        fields = '__all__'

class RequirementSerializer(serializers.ModelSerializer):

    class Meta:
        model = requirement
        fields = '__all__'

class RequirementItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = requirement_item
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = task
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
