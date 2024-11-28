# Generated by Django 5.1.2 on 2024-11-28 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0004_remove_realword_meta_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='realword',
            name='part_of_speech',
            field=models.CharField(blank=True, choices=[('noun', 'Noun'), ('verb', 'Verb'), ('adjective', 'Adjective'), ('adverb', 'Adverb'), ('pronoun', 'Pronoun'), ('preposition', 'Preposition'), ('conjunction', 'Conjunction'), ('interjection', 'Interjection'), ('numeral', 'Numeral'), ('article', 'Article'), ('determiner', 'Determiner')], max_length=20, null=True),
        ),
    ]
