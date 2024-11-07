from django import template
import re

register = template.Library()

@register.filter
def highlight_word(text, word):
    """Выделяет жирным заданное слово в тексте."""
    pattern = re.compile(re.escape(word), re.IGNORECASE)
    highlighted_text = pattern.sub(f'<strong>{word}</strong>', text)
    return highlighted_text
