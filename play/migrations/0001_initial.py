# Generated by Django 5.1.2 on 2024-11-08 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlayPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Default Title', max_length=200)),
                ('name', models.CharField(default='Default Name', max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Play',
                'verbose_name_plural': 'Play',
            },
        ),
    ]
