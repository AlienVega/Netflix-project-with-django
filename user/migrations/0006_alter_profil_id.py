# Generated by Django 4.1.2 on 2022-11-09 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_profil_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]