# Generated by Django 4.2.4 on 2023-08-08 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habbits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, verbose_name='название привычки')),
                ('place', models.CharField(max_length=127, verbose_name='место выполнения')),
                ('times', models.TimeField(default=django.utils.timezone.now, verbose_name='время начала выполнения')),
                ('action', models.CharField(max_length=127, verbose_name='действие')),
                ('good_habit_sign', models.BooleanField(default=False, verbose_name='признак приятной привычки')),
                ('periodicity', models.IntegerField(verbose_name='периодичность')),
                ('reward', models.CharField(max_length=127, verbose_name='вознаграждение')),
                ('execution_time', models.TimeField(default='00:02', verbose_name='время на выполнение')),
                ('is_public', models.BooleanField(default=True, verbose_name='Признак публичности')),
                ('relted_habbit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habbits', verbose_name='связанная привычка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='создатель привычки')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
                'ordering': ['times'],
            },
        ),
    ]