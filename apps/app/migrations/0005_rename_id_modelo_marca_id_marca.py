# Generated by Django 3.2.6 on 2021-12-06 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_nom_tipoproducto_nombre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marca',
            old_name='id_modelo',
            new_name='id_marca',
        ),
    ]