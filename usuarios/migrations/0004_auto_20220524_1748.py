# Generated by Django 3.0 on 2022-05-24 17:48

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20220524_1415'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='usuario',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Usuario está ativo'),
        ),
    ]
