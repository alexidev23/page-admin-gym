# Generated by Django 4.1.7 on 2023-03-27 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0002_alter_clases_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiantes',
            name='documento',
            field=models.IntegerField(max_length=10),
        ),
    ]