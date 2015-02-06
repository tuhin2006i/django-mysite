from django.contrib import admin
from polls.models import Question

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']
    fieldsets = [
	(None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

admin.site.register(Question, QuestionAdmin)
