# Generated by Django 4.0.4 on 2022-07-17 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_move_alter_interaction_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='moves',
            field=models.ManyToManyField(to='main_app.move'),
        ),
    ]
