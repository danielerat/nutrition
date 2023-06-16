from django.contrib import admin
from .models import Conversation, Message, Questionnaire


admin.site.register(Questionnaire)


class MessageInline(admin.TabularInline):
    model = Message
    extra = 1


class QuestionnaireInline(admin.TabularInline):
    model = Questionnaire
    extra = 0
    readonly_fields = [field.name for field in Questionnaire._meta.fields]


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'doctor', 'patient', 'created_at')
    list_filter = ('doctor', 'patient', 'created_at')
    search_fields = ('doctor__username', 'patient__username')
    raw_id_fields = ('doctor', 'patient')
    inlines = [MessageInline, QuestionnaireInline]
