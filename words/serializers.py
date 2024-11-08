# serializers.py
from rest_framework import serializers
from .models import RealWord, Example, Synonym, Antonym

class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ['text']

class SynonymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Synonym
        fields = ['text']

class AntonymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Antonym
        fields = ['text']

class RealWordSerializer(serializers.ModelSerializer):
    examples = ExampleSerializer(many=True, read_only=True)
    synonyms = SynonymSerializer(many=True, read_only=True)
    antonyms = AntonymSerializer(many=True, read_only=True)

    class Meta:
        model = RealWord
        fields = ['word', 'transcription', 'definition', 'image', 'examples', 'synonyms', 'antonyms']
