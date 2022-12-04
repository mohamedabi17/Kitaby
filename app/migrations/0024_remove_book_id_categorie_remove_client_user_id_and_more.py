# Generated by Django 4.1.1 on 2022-12-03 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_remove_user_groups_remove_user_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='id_categorie',
        ),
        migrations.RemoveField(
            model_name='client',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='id_client',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='id_paiment',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='id_user',
        ),
        migrations.RemoveField(
            model_name='lignecommande',
            name='id_book',
        ),
        migrations.RemoveField(
            model_name='lignecommande',
            name='id_categorie',
        ),
        migrations.RemoveField(
            model_name='lignecommande',
            name='id_client',
        ),
        migrations.RemoveField(
            model_name='lignecommande',
            name='id_user',
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Categorie',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Commande',
        ),
        migrations.DeleteModel(
            name='LigneCommande',
        ),
        migrations.DeleteModel(
            name='Paiment',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]