# Generated by Django 4.0.5 on 2022-07-04 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_remove_task_user_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_name',
            field=models.CharField(default='сегодня', max_length=100, null=True, verbose_name='Название даты'),
        ),
        migrations.AlterField(
            model_name='task',
            name='is_executed',
            field=models.BooleanField(default=False, verbose_name='Выполнено'),
        ),
    ]
