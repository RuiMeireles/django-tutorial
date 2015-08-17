from django.contrib import admin

# Register your models here.

from .models import Question, Choice

#1)	MODE 1: Default Registering
#admin.site.register(Question)

#2)	MODE 2: Tell Django the options you want to when registering, and in which order
#class QuestionAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question_text']
#admin.site.register(Question, QuestionAdmin)
    
#3)	MODE 3: Like Mode 2, but split in fieldsets (boxes). Choice is registered using defaults
#class QuestionAdmin(admin.ModelAdmin):
#    fieldsets = [
#        (None,               {'fields': ['question_text']}),
#        #('Date information', {'fields': ['pub_date']}),
#        # Use 'collapse' to hide this fields
#        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#    ]
#admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)

#4)	MODE 4: This tells Django: “Choice objects are edited on the Question admin page. By default, provide enough fields for 3 choices.”
# Stacked Mode - Good when there are few Choices
#class ChoiceInline(admin.StackedInline):
#    model = Choice
#    extra = 3

# Tabular Mode - More compact
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
 
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # This adds other fields to the display (default is only the __str__)
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # This adds a filter sidebar
    list_filter = ['pub_date']
    # This adds search capability
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)