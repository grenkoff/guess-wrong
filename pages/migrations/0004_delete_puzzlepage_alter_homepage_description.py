# Generated by Django 5.1.2 on 2024-10-30 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_puzzlepage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PuzzlePage',
        ),
        migrations.AlterField(
            model_name='homepage',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
