# Generated by Django 5.1.2 on 2024-11-02 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puzzle', '0003_realword_definition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realword',
            name='definition',
            field=models.TextField(default='Default Definition', max_length=1000),
        ),
    ]