# # Generated by Django 4.1.1 on 2022-11-20 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_produit_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='id_categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.categorie'),
        ),
    ]
