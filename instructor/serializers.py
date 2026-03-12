from rest_framework import serializers
from .models import Instructor

import json
from rest_framework import serializers
from .models import Instructor

class InstructorSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(use_url=True, required=False, allow_null=True)

    class Meta:
        model = Instructor
        fields = '__all__'

    def validate_skills(self, value):
        # String kelsa, JSON ga parse qilamiz
        if isinstance(value, str):
            try:
                return json.loads(value)
            except (json.JSONDecodeError, TypeError):
                raise serializers.ValidationError("To'g'ri JSON format kiriting")
        return value

    def validate_achievements(self, value):
        if isinstance(value, str):
            try:
                return json.loads(value)
            except (json.JSONDecodeError, TypeError):
                raise serializers.ValidationError("To'g'ri JSON format kiriting")
        return value
        
class InstructorSerializers(serializers.ModelSerializer):

    class Meta:
        model = Instructor
        fields = "__all__"