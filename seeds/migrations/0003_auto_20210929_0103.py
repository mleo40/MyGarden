# Generated by Django 3.1.5 on 2021-09-29 01:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seeds', '0002_auto_20210929_0040'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlantingBeds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bed_number', models.IntegerField()),
                ('section', models.CharField(choices=[(1, 'Top'), (2, 'Middle'), (3, 'Bottom'), (4, 'Left'), (5, 'Right')], max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='seeds',
            name='sow',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.CreateModel(
            name='Planted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bed_number2', to='seeds.plantingbeds')),
                ('seed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name2', to='seeds.seeds')),
            ],
        ),
    ]
