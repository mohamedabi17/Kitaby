# # Generated by Django 4.1.1 on 2022-11-20 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_produit_id_categorie'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
