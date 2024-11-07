from django.db import models


class Example(models.Model):
    word = models.ForeignKey('RealWord', related_name='examples', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return ""


class Synonym(models.Model):
    word = models.ForeignKey('RealWord', related_name='synonyms', on_delete=models.CASCADE)
    text = models.CharField(max_length=50)

    def __str__(self):
        return ""


class Antonym(models.Model):
    word = models.ForeignKey('RealWord', related_name='antonyms', on_delete=models.CASCADE)
    text = models.CharField(max_length=50)

    def __str__(self):
        return ""


class RealWord(models.Model):
    word = models.CharField(max_length=50, unique=True)
    transcription = models.CharField(max_length=50, blank=True, null=True)
    definition = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.word
