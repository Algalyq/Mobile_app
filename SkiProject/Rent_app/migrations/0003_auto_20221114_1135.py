# Generated by Django 3.2.11 on 2022-11-14 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Rent_app', '0002_uniforms'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seasonticket',
            options={'verbose_name_plural': 'Season ticket'},
        ),
        migrations.AlterModelOptions(
            name='uniforms',
            options={'verbose_name_plural': 'Uniform'},
        ),
    ]