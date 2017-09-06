from django import template
from Chat import backend

# Initializing template library
register = template.Library()

# Tags
@register.assignment_tag
def trainCLF():
    backend.trainCLF()


@register.assignment_tag
def predictAnswer(question):
    return backend.predictAnswer(question_entry=question)


@register.assignment_tag
def storeQAPair(question, answer):
    backend.storeQAPair(question_entry=question, answer_entry=answer)