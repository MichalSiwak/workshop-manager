# Generated by Django 3.0.3 on 2020-02-26 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('car_mechanic', '0003_mechanic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Opis')),
                ('date_added', models.DateField(auto_now_add=True, verbose_name='Data przyjęcia zlecenia')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Data rozpoczęcia pracy')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Data zakończenia pracy')),
                ('estimated_working_time', models.IntegerField(verbose_name='Przewidywany czas pracy ')),
                ('order_status', models.IntegerField(choices=[(1, 'Nieprzydzielone'), (2, 'W toku'), (3, 'Zakończone')], default=1, verbose_name='Zlecenie zakończone')),
                ('number', models.IntegerField(verbose_name='Numer zlecenia')),
                ('mechanic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='car_mechanic.Mechanic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
