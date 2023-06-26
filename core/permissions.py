from rest_framework.permissions import BasePermission
from chat.models import Conversation


class IsConversationParticipant(BasePermission):
    message = "You are not a participant of this conversation."

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        # Retrieve the conversation ID from the URL parameters
        conversation_id = view.kwargs.get('conversation_pk')
        # Retrieve the conversation object
        try:
            conversation = Conversation.objects.get(id=conversation_id)
        except Conversation.DoesNotExist:
            return False
        # Check if the user is a participant of the conversation
        return conversation.patient == request.user or conversation.doctor == request.user
