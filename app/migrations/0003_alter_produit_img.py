# # Generated by Django 4.1.1 on 2022-11-20 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_produit_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='img',
            field=models.CharField(max_length=200),
        ),
    ]