from django import forms
from django.core.exceptions import ValidationError

from django.forms import widgets


from webapp.models import Task


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("status", "teg", "text", "detail_text")
        labels = {
            'status': 'Статус',
            'text': 'Текст',
            'teg': 'Тег',
            'detail_text': 'Детальный текст',
        }

    def clean_text(self):
        text = self.cleaned_data.get("text")
        if len(text) <= 2:
            raise ValidationError("Заполните линию")
        return text
