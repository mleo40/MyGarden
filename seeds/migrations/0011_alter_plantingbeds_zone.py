# Generated by Django 3.2 on 2021-09-29 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seeds', '0010_alter_plantingbeds_zone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantingbeds',
            name='zone',
            field=models.IntegerField(choices=[('Green House', 'Green house'), ('Z1', 'Zone One'), ('Z2', 'Zone Two'), ('Z3', 'Zone Three'), ('Z4', 'Zone Four'), ('Z5', 'Zone Five')], default=1),
        ),
    ]
