# # Generated by Django 4.1.1 on 2022-11-30 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_admin_table_alter_book_table_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='admin',
            table='app_admin',
        ),
        migrations.AlterModelTable(
            name='book',
            table='app_book',
        ),
        migrations.AlterModelTable(
            name='categorie',
            table='app_categorie',
        ),
        migrations.AlterModelTable(
            name='client',
            table='app_client',
        ),
        migrations.AlterModelTable(
            name='commande',
            table='app_commande',
        ),
        migrations.AlterModelTable(
            name='lignecommande',
            table='app_lignecommande',
        ),
        migrations.AlterModelTable(
            name='paiment',
            table='app_paiment',
        ),
        migrations.AlterModelTable(
            name='user',
            table='app_user',
        ),
    ]