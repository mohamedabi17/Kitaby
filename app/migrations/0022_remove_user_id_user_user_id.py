# Generated by Django 4.1.1 on 2022-12-01 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_user_is_active_user_is_staff_alter_user_nom_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id_user',
        ),
        migrations.AddField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
