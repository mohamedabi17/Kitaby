# Generated by Django 4.1.1 on 2022-11-30 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_admin_surname_client_niv_fidélité'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='id_user',
        ),
        migrations.RemoveField(
            model_name='client',
            name='id_user',
        ),
        migrations.AddField(
            model_name='admin',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.user'),
            preserve_default=False,
        ),
    ]