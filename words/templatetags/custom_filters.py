from django import template
import re

register = template.Library()

@register.filter(name='highlight_word')
def highlight_word(text, word):
    # Regular expression to find the word with boundaries and case insensitive
    pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
    
    # Highlight the word
    highlighted_text = pattern.sub(lambda match: f'<strong>{match.group(0)}</strong>', text)

    # Capitalize the first letter of each sentence
    sentences = re.split(r'(\. |\? |\! )', highlighted_text)  # Split on sentence-ending punctuation
    sentences = [sentence[0].upper() + sentence[1:] if sentence else '' for sentence in sentences]
    capitalized_text = ''.join(sentences)
    
    return capitalized_text
