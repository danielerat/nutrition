from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from authentication.models import User
from chat.models import Questionnaire
from .models import Message, Conversation
from django.db import transaction


class SimpleConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ["id", "doctor", "patient", "created_at", "updated_at"]


class QuestionairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = [
            'chronic_diseases', 'activity_level', 'smoking_habits', 'alcohol_consumption',
            'sleep_patterns', 'current_diet', 'food_allergies', 'physical_disability'
        ]
        read_only_fields = ['conversation']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'content', 'created_at']


class ConversationSerializer(serializers.ModelSerializer):
    # messages = MessageSerializer(many=True, read_only=True)
    questionnaire = QuestionairSerializer()

    class Meta:
        model = Conversation
        fields = ['id', 'questionnaire']

    def create(self, validated_data):
        with transaction.atomic():
            questionnaire_data = validated_data.pop('questionnaire')
            patient = self.context.get('user')

            # Create the questionnaire instance first
            questionnaire_serializer = self.fields['questionnaire']
            questionnaire = questionnaire_serializer.create(questionnaire_data)

            # Create the conversation instance and associate the questionnaire
            conversation = Conversation.objects.create(
                patient=patient,
                questionnaire=questionnaire, **validated_data)
            questionnaire.conversation = conversation
            questionnaire.save()
            return conversation
