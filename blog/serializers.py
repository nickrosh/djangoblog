from rest_framework import serializers
from blog.models import Task

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    difficulty = serializers.ChoiceField(choices=Task.DIFFICULTY_CHOICES)

    class Meta:
        model = Task
        fields = ('id', 'user', 'name', 'difficulty', 'description')